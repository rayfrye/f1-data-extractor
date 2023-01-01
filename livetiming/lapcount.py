import logging
import requests
import json
import csv

def GetLapCountData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Lap Count Data")

    Endpoint = 'LapCount.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = response.text

    """
        Session Time
        Lap Count
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/LapCount.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Session Time'
        , 'Current Lap'
    ]
    writer.writerow(header)
    
    for line in data.splitlines():
        splitLine = line.split('{', 1)
        sessionTime = splitLine[0]
        jsonData = json.loads('{' + splitLine[1])
        
        # write a row to the csv file
        row = [
            sessionTime
            , jsonData['CurrentLap']
        ]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting Lap Count data")