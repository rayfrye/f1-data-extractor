import logging
import requests
import json
import csv

def GetRaceControlMessages(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get race control message Data")

    Endpoint = 'RaceControlMessages.json'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = json.loads(response.content)

    """
        Messages
            Utc
            Lap
            Category
            Message
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/RaceControlMessages.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Utc'
        , 'Lap'
        , 'Category'
        , 'Message'
    ]
    writer.writerow(header)

    for message in data['Messages']:
        
        # write a row to the csv file
        row = [
            message['Utc']
            , message['Lap']
            , message['Category']
            , message['Message']
        ]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting race control message data")