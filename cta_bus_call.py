import requests
import urllib

#BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getpredictions'
BUS_LOOKUP = 'http://www.ctabustracker.com/bustime/api/v2/getstops'

#r_south = requests.get(BUS_LOOKUP, params={'key' : 'nfLj3RLeuQimpC6zdQwE3b8qj', 'stpid' : '1813', 'format' : 'json'})
r_south = requests.get(BUS_LOOKUP, params={'key' : 'nfLj3RLeuQimpC6zdQwE3b8qj', 'rt' : '22', 'dir' : 'Southbound', 'format' : 'json'})
print(r_south.text)

#print(r_south.url)
