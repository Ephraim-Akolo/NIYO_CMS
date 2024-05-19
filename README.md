# NIYO_CMS
A simple content management system

## START UP SERVER
Follow the below steps to start up the server.

* Ensure the environmental variables are set and loaded.
* (optional) Create a virtual environment using `python -m venv .venv`. Then activate it and proceed to the next step.
* From the root directory, install dependencies using `python -m pip install -r requirements.txt`.
* From the root directory, migrate the database tables using `python manage.py migrate`.
* Start the gunicorn server on linux environment using `gunicorn core.asgi:application -k uvicorn.workers.UvicornWorker`.


## Environmental Variables


