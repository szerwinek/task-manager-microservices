#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn on port $PORT"
gunicorn auth_service.wsgi:application --bind 0.0.0.0:$PORT
