import json
import time
import requests
import os
from datetime import datetime

API_KEY = os.getenv("LASTFM_API_KEY")
SESSION_KEY = os.getenv("LASTFM_SESSION_KEY")

def scrobble_track(artist, track, timestamp):
    url = "http://ws.audioscrobbler.com/2.0/"
    payload = {
        "method": "track.scrobble",
        "api_key": API_KEY,
        "sk": SESSION_KEY,
        "artist": artist,
        "track": track,
        "timestamp": timestamp,
        "format": "json"
    }
    response = requests.post(url, data=payload)
    print(response.json())

# Get the first file from the directory
folder = "StreamingHistory"
files = sorted(os.listdir(folder))
if files:
    file_to_upload = files[0]
    with open(os.path.join(folder, file_to_upload), "r") as f:
        data = json.load(f)

    for entry in data:
        artist = entry["artistName"]
        track = entry["trackName"]
        timestamp = int(datetime.strptime(entry["time"], "%Y-%m-%dT%H:%M:%SZ").timestamp())
        scrobble_track(artist, track, timestamp)
        time.sleep(0.5)  # Rate limiting

    # Remove uploaded file
    os.remove(os.path.join(folder, file_to_upload))
