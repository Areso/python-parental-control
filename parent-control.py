import ntplib
from time import ctime
import datetime
Network = 0
#setup
#set time, when PC should shut down itself
shutHour = 23
shutMins = 05
shutTotal = shutHour * 60 + shutMins * 1#1385 for 23:05
UTCdiff = 6#UTC+6 Timezone
#room for improvements here... if time is later than 0:00 it should be setuped time when PC allowed to start
#end of setup
Delimeter = ':'
LocalTime = str(datetime.datetime.now())
#print(str(LocalTime))
DelPosLocalTime = LocalTime.find(Delimeter)
LocalTimeHours = int(LocalTime[DelPosLocalTime-2:DelPosLocalTime])
LocalTimeMinutes = int(LocalTime[DelPosLocalTime+1:DelPosLocalTime+3])
LocalTimeTotal = LocalTimeHours * 60 + LocalTimeMinutes
print(str(LocalTimeHours))
print(str(LocalTimeMinutes))
c = ntplib.NTPClient()
try:
    #Response = c.request('europe.pool.ntp.org', version=3)
    Response = c.request('pool.ntp.org')
    NetworkTime = datetime.datetime.utcfromtimestamp(response.tx_time)
    Network = 1
except:
    Network = 0
if Network = 1 
    
#print(newtime)
#print(ctime(response.tx_time))
#print(response.offset)

