import logging
import requests
import zlib
import base64
import json
import csv
    
def GetCarData(BaseURL, Year, RaceID, RaceSession, OutputLocation):

    logging.info("Starting to get Session Data")
    Endpoint = 'CarData.z.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint
    
    logging.info('Connecting to url ' + URL)

    response = requests.get(URL)

    # open the file in the write mode
    f = open(OutputLocation + '/CarData.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = ['Utc', 'Car Number', 'RPM', 'KPH', 'Gear', 'Throttle', 'Brake', 'DRS']
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
        Entries
            Utc
            Cars
                Car
                    Channels
                        0 RPM
                        2 KPH
                        3 Gear
                        4 Throttle %
                        5 Brake on/off
                        45 DRS Open/Closed status - need status mapping
        """
        
        # write a row to the csv file
        for line in Base64DataLines:
        
            lineJson = json.loads(line)
            
            for entry in lineJson['Entries']:
                
                for car in entry['Cars']:
                    channels = entry['Cars'][str(car)]['Channels']                
                    row = [str(entry['Utc']), str(car), channels['0'], channels['2'], channels['3'], channels['4'], channels['5'], channels['45']]
                    writer.writerow(row)

    # close the file
    f.close()
    
    logging.info('Done getting car data')