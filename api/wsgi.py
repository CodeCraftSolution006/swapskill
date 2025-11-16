import os
import sys
from pathlib import Path

# Add the project directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

# Vercel requires a 'handler' function for Python serverless functions
def handler(request):
    """Handler for Vercel Python serverless functions."""
    return app(request)
