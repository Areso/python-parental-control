import ntplib
from time import ctime
import datetime
import os
Network = 0
#setup
#set time, when PC should shut down itself
shutHour  = 23
shutMins  = 05
shutTotal = shutHour * 60 + shutMins * 1#1385 for 23:05
mornHour  = 07
mornMins  = 00
mornTotal = mornHour * 60 + mornMins * 1#420 for 07:00
UTCdiff = 6#UTC+6 Timezone
#end of setup
Delimeter = ':'
LocalTime = str(datetime.datetime.now().time())
#print(str(LocalTime))
DelPosLocalTime = LocalTime.find(Delimeter)
LocalTimeHours = int(LocalTime[DelPosLocalTime-2:DelPosLocalTime])
LocalTimeMinutes = int(LocalTime[DelPosLocalTime+1:DelPosLocalTime+3])
LocalTimeTotal = LocalTimeHours * 60 + LocalTimeMinutes
#print(str(LocalTimeHours))
#print(str(LocalTimeMinutes))
c = ntplib.NTPClient()
NetworkTimeTotal = 0
try:
    Response = c.request('europe.pool.ntp.org', version=3)
    #Response = c.request('pool.ntp.org')
    NetworkTime = str(datetime.datetime.utcfromtimestamp(Response.tx_time))
    DelPosNetworkTime  = NetworkTime.find(Delimeter)
    NetworkTimeHours   = int(NetworkTime[DelPosNetworkTime-2:DelPosNetworkTime])+UTCdiff
    NetworkTimeMinutes = int(NetworkTime[DelPosNetworkTime+1:DelPosNetworkTime+3])
    NetworkTimeTotal   = NetworkTimeHours * 60 + NetworkTimeMinutes
    Network = 1
except:
    Network = 0
print(Network)
print("total local time is ")
print(LocalTimeTotal)
print("total network time is ")
print(NetworkTimeTotal)
print(mornTotal)
print(shutTotal)
if Network == 1: 
    if NetworkTimeTotal > shutTotal or NetworkTimeTotal < mornTotal:
        os.system('systemctl poweroff')
else:
    if LocalTimeTotal > shutTotal or LocalTimeTotal < mornTotal:
        os.system('systemctl poweroff')
