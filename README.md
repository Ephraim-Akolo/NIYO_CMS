# NIYO_CMS
A simple content management system

## START UP SERVER LOCALLY
Follow the below steps to start up the server locally.

* Ensure the environmental variables are set and loaded or a `.env` file is added to the root directory.
* (optional) Create a virtual environment using `python -m venv .venv`. Then activate it and proceed to the next step.
* From the root directory, install dependencies using `pip install -r requirements.txt`.
* From the root directory, migrate the database tables using `python manage.py migrate`.
* Start the server with `python manage.py runserver` or `daphne core.asgi:application -b 0.0.0.0 -p 10000` and it will start at `http://localhost:8000` or `http://0.0.0.0:10000` respectively.
* The live data websocket stream will be available at `ws://localhost:8000/ws/tasks/` or `ws://0.0.0.0:1000/ws/tasks/`

## DEPLOY SERVER
* Ensure the environmental variables are set and loaded
* From the root directory, run the `./build.sh` to install dependencies and make migrations.
* Start the server on linux environment using `daphne core.asgi:application -b 0.0.0.0 -p 10000`.
* The live data websocket stream will be available at `ws://<base_url>/ws/tasks/`


## Environmental Variables

* SECRET_KEY = -3rj%4h#*****    (SECRET_KEY can be generated using `python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
* DATABASE_URL = postgres://user:password@server/database


**Optional environmental variables**


* ALLOWED_HOSTS = localhost 127.0.0.1    (seperate values with spaces)
* CSRF_TRUSTED_ORIGINS = http://localhost http://127.0.0.1   (seperate values with spaces)
* CORS_ALLOWED_ORIGINS = ""

* DEBUG = True
* CORS_ORIGIN_ALLOW_ALL = True
* CORS_ALLOW_CREDENTIALS = True


## TODO

* Containarization (Docker)
