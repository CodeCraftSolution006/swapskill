#!/bin/bash
# Optimized build script for Vercel Python projects
# Runs during the Vercel build phase

set -e

echo "Installing requirements (quiet mode)..."
pip install -q -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build complete!"
