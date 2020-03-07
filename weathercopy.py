import requests
import urllib.parse
import json
import sys

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"id":"2172797","units":"metric","mode":"HTML","q":"boston"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "22aed7585bmshd6d6978096f001ep106573jsn819b5e8a6bd3"
    }

response = requests.get(url, headers=headers, params=querystring)

d = response.text

result = response.json()

json_str = json.dumps(result)

resp = json.loads(json_str)
print (resp['main']["feels_like"])

