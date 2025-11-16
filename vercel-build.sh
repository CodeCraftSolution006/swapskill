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

echo "Build complete!"
