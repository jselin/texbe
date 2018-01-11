#!/bin/sh
 
# Start Gunicorn processes

echo Starting migrations
python3 manage.py migrate

echo Starting Gunicorn.
exec gunicorn texbe.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3