## GETTING STARTED ##
1) make sure that venv is activated `source venv/bin/activate`
2) install dependencies `pip install -r requirements.txt`
3) export server.py `export FLASK_APP=server.py`
4) run local dev server with `flask run`
5) main endpoint is  `/main`

## SETTING UP ENVIRONMENT ##
1) make sure that `.env` file contains correct API keys to connect to db
2) make sure that the video `object_tracking.mp4` is in the `static/videos/` dir
3) video file is accessible via `/video` endpoint