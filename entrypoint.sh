#!/bin/bash
python manage.py wait_for_db
python manage.py makemigrations --noinput
python manage.py migrate --noinput
gunicorn todo.wsgi:application --bind 0.0.0.0:8000
