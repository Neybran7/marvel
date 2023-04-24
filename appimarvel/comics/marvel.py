import requests
import json


private_key = "ae44c373a40cae4d4393c7eb5af469e3324f0c82"
public_key = "620661ca732f53b2798f48cfef87e595"
hashed = "2a47b76bda75a7fcf941a067b556ea90"
laurl = "https://gateway.marvel.com:443/v1/public/series?ts=1&apikey=620661ca732f53b2798f48cfef87e595&hash=2a47b76bda75a7fcf941a067b556ea90"
response = request.get(laurl)
if response.status_code==200:
   response_json = json.loads(response.text)
print(response_json)