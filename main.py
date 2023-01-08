import logging
from livetiming.sessiondata import *
from livetiming.sessioninfo import *
from livetiming.cardata import *
from livetiming.positiondata import *
from livetiming.driverlist import *
from livetiming.racecontrolmessages import *
from livetiming.timingappdata import *
from livetiming.trackstatus import *
from livetiming.weatherdata import *
from livetiming.lapcount import *

BaseURL = 'https://livetiming.formula1.com/static'
#The year you want to pull data for
Year = '2022'
#The race id - not sure if there's a good way to get a comprehensive list of these
RaceID = '2022-10-23_United_States_Grand_Prix'
#There is also data for qualifying, and practice sessions I think
RaceSession = '2022-10-23_Race'
OutputLocation = './output/'

logging.basicConfig(filename='./Log/Log.log', encoding='utf-8', level=logging.DEBUG)

#GetSessionSeriesData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetSessionStatusData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetSessionInfoData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetCarData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetPositionData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetDriverListData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetRaceControlMessages(BaseURL, Year, RaceID, RaceSession, OutputLocation)
GetTimingAppData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetTrackStatusData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetWeatherData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
#GetLapCountData(BaseURL, Year, RaceID, RaceSession, OutputLocation)
