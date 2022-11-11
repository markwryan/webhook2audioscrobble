# plex-audioscrobble-webhook

Use Plex webhook to forward to a audioscrobble service.

## Setup

Assuming python3 is installed.

1. Clone repo and cd into it
2. Create venv
```
python3 -m venv .venv
```
3. Activate venv
```
source .venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Start server
```
python3 app/app.py
```


## Docker Deploy

Build the image with Docker

```
docker build -t plex-audioscrobble-webhook .
```

Run image

```
docker run -p 8000:5000 --name plex-audio-webhook -d plex-audioscrobble-webhook
```
