# Setup Instructions for SkillSwap Django Application

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### 1. Create Virtual Environment
```bash
cd skillswap_project
python -m venv venv
```

### 2. Activate Virtual Environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 6. Run Development Server
```bash
python manage.py runserver
```

The application will be available at: http://127.0.0.1:8000/

## Access the Application

- **Home Page:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Features

### User Authentication
- User registration with email validation
- Secure login/logout
- Password validation
- Profile management

### Skills Management
- Add, edit, and delete skills
- Categorize skills (Programming, Languages, Design, Business, Music, Sports, Cooking, Art, Fitness, Other)
- Skill levels (Beginner, Intermediate, Advanced, Expert)
- Upload skill images
- Browse all skills with search and filter

### Skill Exchange
- Request skill exchanges with other users
- Accept/reject exchange requests
- Mark exchanges as completed
- Leave reviews and ratings

### User Profiles
- View user profiles with skills and reviews
- Profile picture upload
- Bio and location information
- User ratings based on reviews
- Review history

### Database
- SQLite database (automatically created)
- Models for UserProfile, Skill, SkillExchange, and Review

## Project Structure

```
skillswap_project/
├── manage.py
├── requirements.txt
├── README.md
├── config/
│   ├── __init__.py
│   ├── settings.py (Django settings)
│   ├── urls.py (URL routing)
│   └── wsgi.py (WSGI configuration)
├── skillswap/
│   ├── __init__.py
│   ├── admin.py (Admin configuration)
│   ├── apps.py (App configuration)
│   ├── forms.py (Django forms)
│   ├── models.py (Database models)
│   ├── urls.py (App URLs)
│   ├── views.py (View functions)
│   ├── static/ (CSS, JS, images)
│   └── templates/ (HTML templates)
│       └── skillswap/ (App templates)
└── db.sqlite3 (Database file - created after migration)
```

## Default Admin Credentials
After running `python manage.py createsuperuser`, use those credentials to log in to the admin panel.

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, run:
```bash
python manage.py runserver 8080
```

### Database Issues
To reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Missing Migrations
If you encounter migration errors:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Production Deployment

Before deploying to production:
1. Set `DEBUG = False` in settings.py
2. Change `SECRET_KEY` to a secure random string
3. Update `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Configure proper static files handling
7. Set up HTTPS/SSL certificate

## Contact & Support
For issues or questions, please check the Django documentation at https://docs.djangoproject.com/
