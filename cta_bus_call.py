import requests
import json
from credentials import *

#BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getpredictions'
BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getstops'

## Return next busses for the stop by my house.
south_22 = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'stpid' : '1813', 'format' : 'json'})
			# {
			# 	"stpid": "1813",
			# 	"stpnm": "Clark \u0026 Sunnyside",
			# 	"lat": 41.96355882694,
			# 	"lon": -87.666392326355
			# },
north_22 = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'stpid' : '1935', 'format' : 'json'})
			# {
			# 	"stpid": "1935",
			# 	"stpnm": "Clark \u0026 Sunnyside",
			# 	"lat": 41.963351407875,
			# 	"lon": -87.666274309158
			# },
## Printing
#print(south_22.text)
#print(south_22.url)
#print(north_22.text)
#print(north_22.url)

## Return list of all stops on the 22 line
r_south = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'rt' : '22', 'dir' : 'Southbound', 'format' : 'json'})
r_north = requests.get(BUS_LOOKUP, params={'key' : CTA_BUS, 'rt' : '22', 'dir' : 'Northbound', 'format' : 'json'})

## Printing
#print(r_south.text)
#print(r_south.url)
#print(r_north.text)
#print(r_north.url)

# Automatically geolocate the connecting IP
IP_url = 'http://freegeoip.net/json/'
response = requests.get(IP_url)
user_location = json.loads(response.text)
#print(",".join((str(response["latitude"]), str(response["longitude"]))))


# Print bus stop name & coordinates for southbound 22
southbound_stops = json.loads(r_south.text)
for bustime, stops in southbound_stops.items():
	for stop, info in stops.items():
		for values in info:
			print(values['stpnm'], ': ', values['lat'], values['lon'])
