#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Apply database migrations
python manage.py migrate
# Collect static files
python manage.py collectstatic --noinput
# Start Gunicorn server
gunicorn employee-backend.wsgi:application --bind 0.0.0.0:$PORT
