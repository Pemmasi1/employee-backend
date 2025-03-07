#!/bin/bash

# Enable error handling
set -e

# Print each command before executing it
set -x

# Install dependencies
pip install -r requirements.txt

# Retry database migrations up to 5 times
RETRIES=5
until python manage.py migrate; do
  RETRIES=$((RETRIES-1))
  if [ $RETRIES -le 0 ]; then
    echo "Failed to apply database migrations after multiple attempts."
    exit 1
  fi
  echo "Retrying database migrations in 5 seconds..."
  sleep 5
done

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn server
gunicorn employee_backend.wsgi:application --bind 0.0.0.0:$PORT