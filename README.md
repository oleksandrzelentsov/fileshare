# Fileshare

## Configuration

0. Install system requirements:
    - `python3.6` or higher;
    - `postgresql` database engine, create user for app and database;
    - `virtualenv` for installed `python3.6`.

1. Create virtualenv:
```bash
virtualenv -p python3.6 env
. env/bin/activate
```
2. Install requirements:
```bash
pip install -r requirements.txt
```
3. Create `files/local_settings.py` and edit it to your needs (before
that install postgresql database and user for it):
```bash
cp files/local_settings_example.py files/local_settings.py
nano files/local_settings.py
```
4. Using created `local_settings` file run migrations:
```bash
DJANGO_SETTINGS_MODULE=files.local_settings python manage.py migrate
```
You have to have no errors.
5. Run server to check if everything works:
```bash
DJANGO_SETTINGS_MODULE=files.local_settings python manage.py runserver
```
6. Press Ctrl+C to terminate the server and create super user for your
instance:
```bash
DJANGO_SETTINGS_MODULE=files.local_settings python manage.py createsuperuser
```
And answer all the questions.
6. Go to `localhost:8000/admin` in your browser to log into django admin
system.

You're finished configuring.