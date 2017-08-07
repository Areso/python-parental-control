import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version=3)
#response = c.request('pool.ntp.org')
print(ctime(response.tx_time))
print(response)
response.offset
print(response.offset)
response.version
print(response.version)
ctime(response.tx_time)
print(response.tx_time)
ntplib.leap_to_text(response.leap)
print(response.leap)
response.root_delay
print(response.root_delay)
ntplib.ref_id_to_text(response.ref_id)
print(response.ref_id)