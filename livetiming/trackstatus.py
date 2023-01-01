import logging
import requests
import json
import csv

def GetTrackStatusData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Track Status Data")

    Endpoint = 'TrackStatus.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = response.text

    """
        Session Time
        Status
        Message
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/TrackStatus.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Session Time'
        , 'Status'
        , 'Message'
    ]
    writer.writerow(header)
    
    for line in data.splitlines():
        splitLine = line.split('{', 1)
        sessionTime = splitLine[0]
        jsonData = json.loads('{' + splitLine[1])
        
        # write a row to the csv file
        row = [
            sessionTime
            , jsonData['Status']
            , jsonData['Message']
        ]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting Track Status data")