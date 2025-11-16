#!/bin/bash
# Build script for Vercel deployment
# This runs during Vercel's build phase

# Install Python packages (done automatically by Vercel, but explicit here)
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "Build complete!"
