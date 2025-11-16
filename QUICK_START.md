# SkillSwap - Quick Reference Card

## 🚀 Quick Start (Windows)
```
1. Double-click: setup.bat
2. Wait for installation
3. Double-click: run.bat
4. Visit: http://127.0.0.1:8000/
```

## 🚀 Quick Start (Mac/Linux)
```
1. Run: bash setup.sh
2. Run: bash run.sh
3. Visit: http://127.0.0.1:8000/
```

## 📍 Important URLs
| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/register/ |
| Login | http://127.0.0.1:8000/login/ |
| Dashboard | http://127.0.0.1:8000/dashboard/ |
| Browse Skills | http://127.0.0.1:8000/browse-skills/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

## 📊 Database Models

### UserProfile
- Linked to Django User
- bio, profile_picture, location, rating

### Skill
- owner (UserProfile)
- name, description, category, level, image

### SkillExchange
- skill_offered, skill_requested (Skill)
- requester, provider (UserProfile)
- status, message

### Review
- reviewer, reviewee (UserProfile)
- rating (1-5), comment

## 🎯 Main Features

### ✅ Authentication
- Register with email
- Login/Logout
- Profile management

### ✅ Skills
- Add/Edit/Delete
- 10 Categories
- 4 Difficulty Levels
- Image upload

### ✅ Exchange System
- Browse all skills
- Search & filter
- Request exchange
- Accept/reject
- Complete & review

### ✅ Reviews
- Rate other users
- Leave comments
- View rating history
- User scores updated

## 📁 File Structure
```
skillswap_project/
├── setup.bat              (Windows setup)
├── run.bat               (Windows run)
├── setup.sh              (Mac/Linux setup)
├── run.sh                (Mac/Linux run)
├── manage.py             (Django management)
├── requirements.txt      (Dependencies)
├── README.md             (Basic guide)
├── DOCUMENTATION.md      (Full documentation)
├── TESTING.md            (Testing guide)
├── DEPENDENCIES.md       (Dependency info)
├── config/               (Project settings)
├── skillswap/            (Main app)
│   ├── models.py         (Database models)
│   ├── views.py          (View functions)
│   ├── forms.py          (Forms)
│   ├── urls.py           (URL routing)
│   ├── admin.py          (Admin panel)
│   ├── static/           (CSS, JS)
│   └── templates/        (HTML templates)
└── db.sqlite3            (Database - auto-created)
```

## 🔑 Admin Login
```
URL: http://127.0.0.1:8000/admin/
Username: admin
Password: (created during setup)
```

## ⚡ Common Commands

### Setup
```bash
python -m venv venv                    # Create environment
venv\Scripts\activate                  # Activate (Windows)
source venv/bin/activate               # Activate (Mac/Linux)
pip install -r requirements.txt        # Install packages
python manage.py migrate               # Create database
python manage.py createsuperuser       # Create admin
```

### Running
```bash
python manage.py runserver             # Run server
python manage.py runserver 8080        # Run on port 8080
```

### Management
```bash
python manage.py shell                 # Django shell
python manage.py makemigrations        # Create migrations
python manage.py migrate               # Apply migrations
python manage.py createsuperuser       # Create admin account
python manage.py collectstatic         # Collect static files
```

## 🎨 Technology Stack
- **Backend:** Django 4.2.7
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework:** Bootstrap 5
- **Icons:** Font Awesome 6
- **Image Processing:** Pillow

## 🐛 Troubleshooting

### Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Port in Use
```bash
python manage.py runserver 8080
```

### Reset Database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Missing Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📞 Support Resources
- Django Docs: https://docs.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- Font Awesome: https://fontawesome.com/
- Python: https://www.python.org/

## ✨ Features Summary
✅ User Authentication & Registration
✅ Profile Management with Picture Upload
✅ Skill Management (CRUD operations)
✅ Advanced Skill Search & Filter
✅ Skill Exchange Request System
✅ Exchange Status Management
✅ User Review & Rating System
✅ Responsive Bootstrap UI
✅ SQLite Database
✅ Django Admin Panel
✅ Production Ready Code
✅ Complete Documentation

## 🎓 Learning Outcomes
By using this app, you'll learn:
- Django project structure
- Django ORM (Models)
- Django Views & URL routing
- Django Forms & Validation
- Template inheritance
- User authentication
- Database design
- RESTful concepts
- Bootstrap 5
- HTML/CSS/JavaScript

## 📄 Version Info
- **Version:** 1.0
- **Created:** 2025
- **Status:** Production Ready
- **License:** Free to use and modify

---

**Start with:** setup.bat (Windows) or setup.sh (Mac/Linux)
**Then run:** run.bat (Windows) or run.sh (Mac/Linux)
**Visit:** http://127.0.0.1:8000/

Happy Coding! 🚀
