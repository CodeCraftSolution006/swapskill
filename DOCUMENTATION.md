# SkillSwap - Full Functional Django Web Application

## Overview
SkillSwap is a complete web application built with Django and SQLite that allows users to share and exchange skills with others in their community. It features user authentication, skill management, exchange requests, and a rating system.

## ✨ Key Features

### 1. **User Authentication & Registration**
   - User registration with email validation
   - Secure login/logout functionality
   - Password validation and strength requirements
   - Profile creation for new users

### 2. **Profile Management**
   - User profiles with bio and location
   - Profile picture upload
   - User rating system based on reviews
   - Review history

### 3. **Skill Management**
   - Add, edit, delete skills
   - 10 skill categories (Programming, Languages, Design, Business, Music, Sports, Cooking, Art, Fitness, Other)
   - 4 skill levels (Beginner, Intermediate, Advanced, Expert)
   - Skill image upload
   - Detailed skill descriptions

### 4. **Skill Exchange**
   - Browse all available skills
   - Search and filter skills by category
   - Request skill exchanges
   - Accept/reject exchange requests
   - Mark exchanges as completed

### 5. **Review & Rating System**
   - Leave reviews after completed exchanges
   - Rate users from 1-5 stars
   - View user ratings and review history
   - Comments on exchanges

### 6. **Database**
   - SQLite database (lightweight and included)
   - 4 main models: UserProfile, Skill, SkillExchange, Review
   - Automatic relationships and constraints

## 🚀 Quick Start

### Windows Users
Simply double-click `setup.bat` and follow the prompts:
```bash
setup.bat
```

### Mac/Linux Users
Run the setup script:
```bash
bash setup.sh
```

### Manual Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin Account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
skillswap_project/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
├── setup.bat                    # Windows setup script
├── setup.sh                     # Linux/Mac setup script
│
├── config/                      # Project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── skillswap/                   # Main app directory
│   ├── admin.py                # Django admin configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Django forms (registration, skills, etc.)
│   ├── models.py               # Database models
│   ├── urls.py                 # App URL patterns
│   ├── views.py                # View functions (controllers)
│   │
│   ├── static/                 # Static files
│   │   ├── css/
│   │   └── js/
│   │
│   └── templates/              # HTML templates
│       ├── base.html           # Base template with navigation
│       └── skillswap/
│           ├── index.html              # Home page
│           ├── register.html           # Registration page
│           ├── login.html              # Login page
│           ├── dashboard.html          # User dashboard
│           ├── profile.html            # User profile view
│           ├── profile_edit.html       # Edit profile
│           ├── skill_form.html         # Add/edit skill
│           ├── skill_detail.html       # View skill details
│           ├── browse_skills.html      # Browse all skills
│           ├── exchange_request.html   # Request exchange
│           ├── exchange_respond.html   # Respond to exchange
│           ├── review_form.html        # Leave review
│           └── skill_confirm_delete.html # Delete skill
│
└── db.sqlite3                  # SQLite database (created after migration)
```

## 🗄️ Database Models

### UserProfile
- One-to-one relationship with Django's User model
- Fields: bio, profile_picture, location, rating, created_at, updated_at

### Skill
- Foreign key to UserProfile (owner)
- Fields: name, description, category, level, image, created_at, updated_at
- Categories: programming, languages, design, business, music, sports, cooking, art, fitness, other
- Levels: beginner, intermediate, advanced, expert

### SkillExchange
- Foreign keys to Skill (offered and requested) and UserProfile (requester and provider)
- Fields: status, message, created_at, updated_at
- Status options: pending, accepted, completed, rejected, cancelled

### Review
- Foreign keys to UserProfile (reviewer and reviewee) and SkillExchange
- Fields: rating (1-5), comment, created_at
- Unique constraint: one review per reviewer-reviewee-exchange combination

## 🔐 Authentication & Security

- Django's built-in authentication system
- Password hashing using PBKDF2 with SHA256
- Email validation on registration
- CSRF protection on all forms
- Session-based user authentication

## 🎨 Frontend

- Bootstrap 5 for responsive design
- Custom CSS with modern gradient styling
- Font Awesome icons
- Responsive mobile-friendly layout
- Interactive forms with validation

## 📊 API Endpoints

### Authentication
- `POST /register/` - User registration
- `POST /login/` - User login
- `GET /logout/` - User logout

### Profiles
- `GET /profile/<username>/` - View user profile
- `GET /profile/edit/` - Edit own profile (requires login)
- `POST /profile/edit/` - Save profile changes

### Skills
- `GET /` - Home page with featured skills
- `GET /browse-skills/` - Browse all skills with filters
- `GET /skill/<id>/` - View skill details
- `GET /skill/create/` - Add new skill form (requires login)
- `POST /skill/create/` - Save new skill
- `GET /skill/<id>/edit/` - Edit skill form
- `POST /skill/<id>/edit/` - Save skill changes
- `GET /skill/<id>/delete/` - Delete skill confirmation
- `POST /skill/<id>/delete/` - Delete skill

### Exchanges
- `GET /exchange/<skill_id>/request/` - Exchange request form
- `POST /exchange/<skill_id>/request/` - Submit exchange request
- `GET /exchange/<exchange_id>/respond/` - Respond to exchange request
- `POST /exchange/<exchange_id>/respond/` - Accept or reject request
- `GET /exchange/<exchange_id>/complete/` - Mark exchange as complete
- `GET /review/<exchange_id>/create/` - Leave review form
- `POST /review/<exchange_id>/create/` - Submit review

### Dashboard
- `GET /dashboard/` - User dashboard with stats (requires login)

## 🔧 Configuration

### settings.py
- Database: SQLite3
- Debug: True (development)
- Allowed hosts: * (development)
- Installed apps: Django built-ins + skillswap
- Templates directory: `skillswap/templates/`
- Static files directory: `skillswap/static/`
- Media files directory: `media/`

## 📝 Usage Guide

### Creating an Account
1. Click "Register" on the homepage
2. Fill in username, email, password
3. Click "Register"
4. You'll be redirected to login
5. Login with your credentials

### Adding a Skill
1. Login to your account
2. Click "Add Skill" in navigation
3. Fill in skill details (name, category, level, description, optional image)
4. Click "Create Skill"

### Browsing & Searching Skills
1. Click "Browse Skills" in navigation
2. Use search box to find skills by name
3. Use category dropdown to filter
4. Click "Filter" to apply filters
5. Click "View Details" on any skill

### Requesting an Exchange
1. View a skill you're interested in
2. Click "Request Exchange"
3. Select a skill from your collection to offer
4. Add an optional message
5. Click "Send Exchange Request"

### Responding to Requests
1. Go to Dashboard
2. Find pending exchange requests
3. Click "Respond"
4. Click "Accept Exchange" or "Reject"

### Completing & Rating
1. After accepting an exchange, meet and complete the skill exchange
2. Go to Dashboard and click "Mark Complete"
3. You'll be prompted to leave a review
4. Rate the user and add comments
5. Submit review

### Editing Your Profile
1. Click your username dropdown
2. Select "Edit Profile"
3. Update your information
4. Click "Save Changes"

## 🐛 Troubleshooting

### Virtual Environment Issues
- On Windows: Use `venv\Scripts\activate`
- On Mac/Linux: Use `source venv/bin/activate`
- If it doesn't work, reinstall: `python -m venv venv`

### Port Already in Use
```bash
python manage.py runserver 8080
```

### Database Errors
Reset database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Dependencies Won't Install
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

## 🚢 Deployment Checklist

Before deploying to production:
- [ ] Set `DEBUG = False`
- [ ] Generate a new `SECRET_KEY`
- [ ] Set `ALLOWED_HOSTS` to your domain
- [ ] Use PostgreSQL instead of SQLite
- [ ] Configure proper static files serving
- [ ] Set up HTTPS/SSL
- [ ] Use a production WSGI server (Gunicorn)
- [ ] Set up proper error logging
- [ ] Configure email backend for password resets
- [ ] Add rate limiting
- [ ] Set up database backups

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Forms](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.3/)

## 📄 License

This is a free educational project. Feel free to modify and use as needed.

## 💡 Future Enhancements

- Real-time notifications
- Messaging system between users
- Advanced user search/discovery
- Skill endorsements
- Skill certificates
- Mobile app version
- Payment integration for premium features
- Video tutorials
- API for third-party integrations

## 🤝 Contributing

This is a learning project. Feel free to extend it with:
- Additional features
- Better UI/UX
- Performance optimizations
- Testing
- Documentation improvements

---

**Created:** 2025
**Version:** 1.0
**Status:** Production Ready

Enjoy using SkillSwap! 🚀
