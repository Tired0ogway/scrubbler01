import hashlib

import requests

API_KEY = ""
SECRET = ""
TOKEN = ""

# Generate API signature
api_sig_str = f"api_key{API_KEY}methodauth.getSessiontoken{TOKEN}{SECRET}"
api_sig = hashlib.md5(api_sig_str.encode()).hexdigest()

url = f"http://ws.audioscrobbler.com/2.0/?method=auth.getSession&api_key={API_KEY}&token={TOKEN}&api_sig={api_sig}&format=json"
response = requests.get(url)
session_key = response.json()["session"]["key"]
print(f"Your session key: {session_key}")
    
