import os
import django

from vercel_wsgi import handle_wsgi_request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

def handler(request, context):
    """Vercel handler that adapts Django WSGI app to Vercel's Python runtime."""
    return handle_wsgi_request(application, request, context)
