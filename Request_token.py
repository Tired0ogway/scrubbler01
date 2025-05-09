import requests

API_KEY = ""
SECRET = ""

url = f"http://ws.audioscrobbler.com/2.0/?method=auth.getToken&api_key={API_KEY}&format=json"
response = requests.get(url)
token = response.json()["token"]
print(f"Go to this URL to authorize: https://www.last.fm/api/auth/?api_key={API_KEY}&token={token}")
