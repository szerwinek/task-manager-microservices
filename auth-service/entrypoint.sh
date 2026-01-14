#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
exec gunicorn auth_service.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 1 \
    --threads 2
