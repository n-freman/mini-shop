#!/usr/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn core.wsgi:application --reload --bind 0.0.0.0:8000
