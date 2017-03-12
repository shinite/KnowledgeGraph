import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '09448c2ffb4144eabfebbd6dfe0d0d35',
}

query = raw_input()

params = urllib.urlencode({
    # Request parameters
    'q': query,
    'count': '1',
    'offset': '0',
    'mkt': 'en-us',
    'safesearch': 'Moderate',
})

try:
    conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
    conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))