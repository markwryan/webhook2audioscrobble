# webhook2audioscrobble

Use Plex webhook to forward to a audioscrobble service, specifically a self-hosted instance of [Maloja](https://github.com/krateng/maloja).

## Running Locally

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


## Docker Deploy via Compose
Example`docker-compose.yaml` is provided.

### Setup for Plex and Maloja
Assuming you have Plex and Maloja running:
1. Log into Maloja admin and navigate to API Keys (/admin_apikeys)
2. Create new API Key and copy it
3. Update the `docker-compose.yaml` to set SCROBBLE_URL to `[maloja url]/apis/mlj_1/newscrobble` (e.g. `http://localhost:42010/apis/mlj_1/newscrobble`)
4. Update the `docker-compose.yaml` to set SCROBBLE_API_KEY to your new API Key you created in Maloja
5. Deploy docker
6. Add new Plex webhook at `[plex server url]/web/index.html#!/settings/webhooks` pointing to `[plex-audioscrobble-webhook url]:42011`

## Build for Linux amd64

```
docker buildx build --platform linux/amd64 -t markwryan/plex-audioscrobble-webhook:latest --push .
```
