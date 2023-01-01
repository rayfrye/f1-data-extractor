import logging
import requests
import json
import csv

def GetSessionSeriesData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Session Series Data")

    Endpoint = 'SessionData.json'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = json.loads(response.content)

    """
        Series
            Utc
            Lap
        StatusSeries
            Utc
            TrackStatus
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/SessionDataSeries.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = ['Utc', 'Lap']
    writer.writerow(header)

    # write a row to the csv file
    for record in data['Series']:
        row = [str(record['Utc']), str(record['Lap'])]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting session series data")

def GetSessionStatusData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Session Status Data")

    Endpoint = 'SessionData.json'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = json.loads(response.content)

    """
        Series
            Utc
            Lap
        StatusSeries
            Utc
            TrackStatus
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/SessionDataStatus.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = ['Utc', 'TrackStatus']
    writer.writerow(header)

    # write a row to the csv file
    for record in data['StatusSeries']:
        if "TrackStatus" in record:
            row = [str(record['Utc']), record['TrackStatus']]
            writer.writerow(row)
        elif "SessionStatus" in record:
            row = [str(record['Utc']), record['SessionStatus']]
            writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting session status data")