import logging
import requests
import json
import csv

def GetWeatherData(BaseURL, Year, RaceID, RaceSession, OutputLocation):
    
    logging.info("Starting to get Weather Data")

    Endpoint = 'WeatherData.jsonStream'
    URL = BaseURL + '/' + Year + '/' + RaceID + '/' + RaceSession + '/' + Endpoint

    logging.info ('Connecting to url ' + URL)

    response = requests.get(URL)

    data = response.text

    """
        Session Time
        Air Temp
        Humidity
        Pressure
        Rainfall
        Track Temp
        Wind Direction
        Wind Speed
    """
        
    # open the file in the write mode
    f = open(OutputLocation + '/WeatherData.csv', 'w')

    # create the csv writer
    writer = csv.writer(f)
    header = [
        'Session Time'
        , 'Air Temp'
        , 'Humidity'
        , 'Pressure'
        , 'Rainfall'
        , 'Track Temp'
        , 'Wind Direction'
        , 'Wind Speed'
    ]
    writer.writerow(header)
    
    for line in data.splitlines():
        splitLine = line.split('{', 1)
        sessionTime = splitLine[0]
        jsonData = json.loads('{' + splitLine[1])
        
        # write a row to the csv file
        row = [
            sessionTime
            , jsonData['AirTemp']
            , jsonData['Humidity']
            , jsonData['Pressure']
            , jsonData['Rainfall']
            , jsonData['TrackTemp']
            , jsonData['WindDirection']
            , jsonData['WindSpeed']
        ]
        writer.writerow(row)

    # close the file
    f.close()
    
    logging.info ("Done Getting Weather data")