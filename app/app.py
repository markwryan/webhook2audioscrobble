#!/usr/bin/python
import os
import json
import requests
from flask import Flask, request

app = Flask(__name__)

scrobble_url = os.getenv("SCROBBLE_URL")
api_key = os.getenv("SCROBBLE_API_KEY")

@app.route('/', methods=['POST'])
def home():
    data = json.loads(request.form['payload'])
    print(data)

    is_scrobble = data['event'] == 'media.scrobble'
    is_audio_track = data['Metadata']['type'] == 'track'
    if is_scrobble and is_audio_track:
        title = data['Metadata']['title']
        album = data['Metadata']['parentTitle']
        artist = data['Metadata']['grandparentTitle']
        if artist == 'Various Artists':
            artist = data['Metadata']['originalTitle']
        response = requests.post(scrobble_url, json={'artist': artist, 'album': album, 'title': title, 'key': api_key})
    return ''

if __name__ == '__main__':
    app.run()