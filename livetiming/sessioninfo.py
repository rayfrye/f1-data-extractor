import logging
import requests
import json
import csv

def GetSessionInfoData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Session Info Data")

    Endpoint = 'SessionInfo.json'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = json.loads(response.content)

    """
        Meeting
            Key
            Name
            OfficialName
            Location
            Country
                Key
                Code
                Name
            Circuit
                Key
                ShortName
        ArchiveStatus
            Status
        Key
        Type
        Name
        StartDate
        EndDate
        GmtOffset
        Path
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/SessionInfo.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Meeting Key'
        , 'Meeting Name'
        , 'Meeting Official Name'
        , 'Meeting Location'
        , 'Meeting Country Key'
        , 'Meeting Country Code'
        , 'Meeting Country Name'
        , 'Meeting Circuit Key'
        , 'Meeting Circuit Short Name'
        , 'Archive Status'
        , 'Key'
        , 'Type'
        , 'Name'
        , 'Start Date'
        , 'End Date'
        , 'Gmt Offset'
        , 'Path'
    ]
    writer.writerow(header)

    # write a row to the csv file
    MeetingKey = str(data['Meeting']['Key'])
    MeetingName = data['Meeting']['Name']
    MeetingOfficialName = data['Meeting']['OfficialName']
    MeetingCountryKey = str(data['Meeting']['Country']['Key'])
    MeetingCountryCode = data['Meeting']['Country']['Code']
    MeetingCountryName = data['Meeting']['Country']['Name']
    MeetingCircuitKey = str(data['Meeting']['Circuit']['Key'])
    MeetingCircuitShortName = data['Meeting']['Circuit']['ShortName']
    ArchiveStatus = data['ArchiveStatus']['Status']
    Key = str(data['Key'])
    Type = data['Type']
    Name = data['Name']
    StartDate = data['StartDate']
    EndDate = data['EndDate']
    GmtOffset = data['GmtOffset']
    Path = data['Path']
    row = [
        MeetingKey
        , MeetingName
        , MeetingOfficialName
        , MeetingCountryKey
        , MeetingCountryCode
        , MeetingCountryName
        , MeetingCircuitKey
        , MeetingCircuitShortName
        , ArchiveStatus
        , Key
        , Type
        , Name
        , StartDate
        , EndDate
        , GmtOffset
        , Path
    ]
    writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting session Info data")