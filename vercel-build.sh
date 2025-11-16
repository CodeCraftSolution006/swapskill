#!/bin/bash
# Build script for Vercel Python projects
# Runs during the Vercel build phase

set -e

echo "Installing dependencies..."
pip install --upgrade pip setuptools wheel

echo "Installing requirements..."
pip install -r requirements.txt

echo "Running Django migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Creating superuser if needed..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@skillswap.com', 'admin123')
    print("Superuser created successfully")
else:
    print("Superuser already exists")
END

echo "Build complete!"
