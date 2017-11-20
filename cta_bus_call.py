import requests
import urllib

BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getstops'

params = {'key': 'nfLj3RLeuQimpC6zdQwE3b8qj', 'rt': 22, 'dir': "South Bound"}
params = urllib.parse.urlencode(params)
r_south = requests.get(BUS_LOOKUP, params)

# print(r_south.text)

print(r_south.url)
