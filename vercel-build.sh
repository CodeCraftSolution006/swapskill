#!/bin/bash
# Build script for Vercel Python projects

set -e

echo "Installing requirements..."
pip install -q -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build complete!"
