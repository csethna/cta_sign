import requests
import json

STATION_URL = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'

r_south = requests.get(STATION_URL, params={'key': 'nfLj3RLeuQimpC6zdQwE3b8qj', 'mapid': '40540', 'stpid': '30106', 'max': '2'})

r_north = requests.get(STATION_URL, params={'key': 'nfLj3RLeuQimpC6zdQwE3b8qj', 'mapid': '40540', 'stpid': '30105', 'max': '2'})

print(r_south.text)

# print('Red line to 95/ Dan Ryan:' + r_south)
# print('Red line to Howard:' + r_north)
