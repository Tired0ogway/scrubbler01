import json
import time
import requests

API_KEY = "6267962a5e22a210191c11109c814dd3"
SESSION_KEY = "xqQs8zyEAYkytO4PdabytcRr7yxmACYv"

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

# Load Spotify listening history
with open("StreamingHistory.json", "r") as f:
    data = json.load(f)

# Send each track to Last.fm
for entry in data:
    artist = entry["artistName"]
    track = entry["trackName"]
    timestamp = int(time.mktime(time.strptime(entry["endTime"], "%Y-%m-%d %H:%M")))
    scrobble_track(artist, track, timestamp)
    time.sleep(0.5)  # Rate limiting

