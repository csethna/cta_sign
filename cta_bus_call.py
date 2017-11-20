import requests
import urllib3
import json
from credentials import *

#BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getpredictions'
BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getstops'

#r_south = requests.get(BUS_LOOKUP, params={'key' : 'nfLj3RLeuQimpC6zdQwE3b8qj', 'stpid' : '1813', 'format' : 'json'})
r_south = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'rt' : '22', 'dir' : 'Southbound', 'format' : 'json'})
r_north = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'rt' : '22', 'dir' : 'Northbound', 'format' : 'json'})
#print(r_south.text)
#print(r_south.url)
#print(r_north.text)
#print(r_north.url)

# Automatically geolocate the connecting IP
http = urllib3.PoolManager()
IP_url = 'http://freegeoip.net/json/'
response = http.request('GET', IP_url)
response = str(response)
#location = json.loads(response)
print(response)
# location_city = location['city']
# location_state = location['region_name']
# location_country = location['country_name']
# location_zip = location['zipcode']
