import requests
import urllib

BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getstops?key=nfLj3RLeuQimpC6zdQwE3b8qj&rt=22&dir=South%20Bound'

r_south = requests.get(BUS_LOOKUP)

print(r_south.text)

#print(r_south.url)
