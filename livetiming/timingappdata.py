import logging
import requests
import json
import csv

def GetTimingAppData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get timing app Data")

    Endpoint = 'TimingAppData.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = response.text#json.loads(response.content)

    """
        Session Time
        Lines
            Car
                Number int
                Line
                GridPos
                Stints
                    Number
                    LapFlags int
                    Number int
                    Compound str
                    New bool
                    TyresNotChanged int
                    TotalLaps int
                    StartLaps int
                    LapNumber int
                    LapTime str
    """

    # open the file in the write mode
    f = open(OutputLocation + '/TimingAppData.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Session Time'
        , 'Car Number'
        , 'Line'
        , 'Grid Position'
        , 'Stints'
        , 'Lap Time'
        , 'Lap Flags'
        , 'Lap Number'
        , 'Compound'
        , 'New'
        , 'Tyres Not Changed'
        , 'Total Laps'
        , 'Start Laps'
    ]
    writer.writerow(header)
    
    for line in data.splitlines():
        #data comes in with session time on the same line as the json data
        #but not actually in the json element, so we need to
        #break session time portion off from actual json stuff
        splitLine = line.split('{', 1)
        
        sessionTime = splitLine[0]
        jsonData = json.loads('{' + splitLine[1])

        for carNumber in jsonData['Lines']:
            jsonLine = jsonData['Lines'][str(carNumber)]
            
            # Set default values for each property
            # then check to see if the key exists in the
            # data, and use it if it does
            Line = -1
            if 'Line' in jsonLine:
                Line = jsonLine['Line']
                
            GridPosition = -1
            if 'GridPos' in jsonLine:
                GridPosition = jsonLine['GridPos']
                
            Stints = -1
            LapTime = ''
            LapFlags = -1
            LapNumber = -1
            Compound = 'UNKONWN'
            New = False
            TyresNotChanged = -1
            TotalLaps = -1
            StartLaps = -1
            if 'Stints' in jsonLine:
                for Stints in jsonLine['Stints']:
                    StintProps = jsonLine['Stints'][str(Stints)]
                    if 'LapTime' in StintProps:
                        LapTime = StintProps['LapTime']
                    if 'LapFlags' in StintProps:
                        LapFlags = StintProps['LapFlags']
                    if 'LapNumber' in StintProps:
                        LapNumber = StintProps['LapNumber']
                    if 'Compound' in StintProps:
                        Compound = StintProps['Compound']
                    if 'New' in StintProps:
                        New = StintProps['New']
                    if 'TyresNotChanged' in StintProps:
                        TyresNotChanged = StintProps['TyresNotChanged']
                    if 'TotalLaps' in StintProps:
                        TotalLaps = StintProps['TotalLaps']
                    if 'StartLaps' in StintProps:
                        StartLaps = StintProps['StartLaps']
                    
                
            # write a row to the csv file
            row = [
                sessionTime
                , carNumber
                , Line
                , GridPosition
                , Stints
                , LapTime
                , LapFlags
                , LapNumber
                , Compound
                , New
                , TyresNotChanged
                , TotalLaps
                , StartLaps
            ]
            writer.writerow(row)
            
    # close the file
    f.close()
    
    logging.info ("Done Getting timing app data")