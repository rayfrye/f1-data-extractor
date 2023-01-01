import logging
import requests
import json
import csv

def GetDriverListData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Driver List Data")

    Endpoint = 'DriverList.json'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = json.loads(response.content)

    """
        Driver
            RacingNumber
            BroadcastName
            FullName
            Tla
            Line
            TeamName
            TeamColour
            FirstName
            LastName
            Reference
            HeadshotUrl
            CountryCode
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/DriverList.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'RacingNumber'
        , 'BroadcastName'
        , 'FullName'
        , 'Tla'
        , 'Line'
        , 'TeamName'
        , 'TeamColour'
        , 'FirstName'
        , 'LastName'
        , 'Reference'
        , 'HeadshotUrl'
        , 'CountryCode'
    ]
    writer.writerow(header)
    for car in data:
        # Need to handle headshot url separately because apparently
        # kmag has no headshot url.
        # It might be a good idea to handle all the properties this way, but eh. 
        headshotUrl = ''
        if 'HeadshotUrl' in data[car]:
            headshotUrl = data[car]['HeadshotUrl']
        # write a row to the csv file
        row = [
            data[car]['RacingNumber']
            , data[car]['BroadcastName']
            , data[car]['FullName']
            , data[car]['Tla']
            , data[car]['Line']
            , data[car]['TeamName']
            , data[car]['TeamColour']
            , data[car]['FirstName']
            , data[car]['LastName']
            , data[car]['Reference']
            , headshotUrl
            , data[car]['CountryCode']
        ]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting Driver List data")