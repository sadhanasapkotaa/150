#!/bin/bash

echo "=== BUILD ==="
pip install -r requirements/production.txt

echo "=== RELEASE ==="
python manage.py migrate
python manage.py collectstatic --noinput

echo "=== RUN ==="
gunicorn config.wsgi:application --bind 0.0.0.0:8000