import json
import urllib

api_key = 'AIzaSyBoO6U5yu0b9z47-rEXy5HQpErIWec_8bc'
query = raw_input()
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 1,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
for element in response['itemListElement']:
  print element['result']['detailedDescription']['articleBody'] 