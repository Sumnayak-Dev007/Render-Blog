#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files without user input
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create a superuser if CREATE_SUPERUSER environment variable is set
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
