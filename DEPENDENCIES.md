# SkillSwap Project - Required Dependencies

## Core Framework
- Django==4.2.7 - Web framework for Python

## Image Processing
- Pillow==10.1.0 - Python imaging library (for image upload/processing)

## Configuration Management
- python-decouple==3.8 - Environment variables management

## Usage
All dependencies can be installed with:
```bash
pip install -r requirements.txt
```

## Optional Dependencies (for production)
- gunicorn - WSGI HTTP Server
- psycopg2-binary - PostgreSQL adapter
- django-cors-headers - CORS handling
- django-dotenv - Environment variables
- whitenoise - Static files serving
- django-extensions - Additional management commands

Install with:
```bash
pip install gunicorn psycopg2-binary django-cors-headers django-dotenv whitenoise django-extensions
```
