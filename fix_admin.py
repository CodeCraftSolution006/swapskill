#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

# Delete existing admin if exists
User.objects.filter(username='admin').delete()

# Create new admin user
admin = User.objects.create_superuser(
    username='admin',
    email='admin@skillswap.com',
    password='admin@123'
)

print("=" * 50)
print("✅ Admin Account Created Successfully!")
print("=" * 50)
print(f"Username: admin")
print(f"Password: admin@123")
print(f"Email: admin@skillswap.com")
print("=" * 50)
print("Login at: http://127.0.0.1:8000/admin/")
print("=" * 50)
