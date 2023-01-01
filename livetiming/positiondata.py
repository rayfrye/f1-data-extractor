import logging
import requests
import zlib
import base64
import json
import csv

def GetPositionData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    logging.info("Starting to get Position Data")

    Endpoint = 'Position.z.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info('Connecting to url ' + URL)

    response = requests.get(URL)

    # open the file in the write mode
    f = open(OutputLocation + '/PositionData.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = ['Utc', 'Car Number', 'Status', 'X', 'Y', 'Z']
    writer.writerow(header)

    for record in response.text.splitlines():
        """
            Logtime?
            Base64Data
        """
        
        splitRecord = record.split("\"")
        
        Utc = str(splitRecord[0])
        unzipped = zlib.decompress(base64.b64decode(str(splitRecord[1])), -zlib.MAX_WBITS)
        Base64Data = unzipped.decode('utf-8-sig')
        Base64DataLines = Base64Data.splitlines()
        """
        Position
            Utc
            Entries
                Car
                    Status
                    X
                    Y
                    Z
        """
        
        # write a row to the csv file
        for line in Base64DataLines:
        
            lineJson = json.loads(line)
            
            for position in lineJson['Position']:
                timestamp = position['Timestamp']
                
                for car in position['Entries']:
                    
                    status = position['Entries'][str(car)]['Status']
                    x = position['Entries'][str(car)]['X']
                    y = position['Entries'][str(car)]['Y']
                    z = position['Entries'][str(car)]['Z']
                    row = [timestamp, str(car), status, x, y, z]
                    writer.writerow(row)

    # close the file
    f.close()