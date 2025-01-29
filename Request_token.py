import requests

API_KEY = "6267962a5e22a210191c11109c814dd3"
SECRET = "aad952b66ed4651379314b01173bc395"

url = f"http://ws.audioscrobbler.com/2.0/?method=auth.getToken&api_key={API_KEY}&format=json"
response = requests.get(url)
token = response.json()["token"]
print(f"Go to this URL to authorize: https://www.last.fm/api/auth/?api_key={API_KEY}&token={token}")
