# Vercel Deployment Guide - SkillSwap

## Overview
This guide will walk you through deploying the SkillSwap project to Vercel with proper database configuration.

## Prerequisites
- GitHub account with the repository pushed
- Vercel account (https://vercel.com)
- Optional: PostgreSQL database (Supabase, Neon, or Railway)

## Step 1: Deploy to Vercel

### Option A: Using Vercel Dashboard (Recommended)
1. Go to https://vercel.com/dashboard
2. Click **"Add New"** → **"Project"**
3. Select **"Import Git Repository"**
4. Find and select `CodeCraftSolution006/swapskill`
5. Click **"Import"**

### Option B: Using Vercel CLI
```bash
npm i -g vercel
vercel --prod
```

## Step 2: Configure Environment Variables

After importing the project in Vercel, go to:
**Project Settings → Environment Variables**

Add the following variables:

### Required Variables

**1. SECRET_KEY** (Generate a new one)
```bash
# Generate locally with:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
- **Key:** `SECRET_KEY`
- **Value:** `django-insecure-<your-generated-key>`

**2. DEBUG**
- **Key:** `DEBUG`
- **Value:** `False`

**3. ALLOWED_HOSTS**
- **Key:** `ALLOWED_HOSTS`
- **Value:** `your-domain.vercel.app` (Vercel will provide this after first deploy)

### Database Configuration (Choose One)

#### Option A: Local SQLite (Default - No Additional Setup)
The app uses SQLite by default if no DATABASE_URL is set. Data will be stored in the `/tmp` directory (not persistent between deploys).

#### Option B: PostgreSQL (Recommended for Production - Persistent Data)

Choose one of these services for a free PostgreSQL database:

##### 1. Supabase (Recommended)
1. Go to https://supabase.com
2. Sign up and create a new project
3. Go to **Project Settings → Database**
4. Copy the connection string (URI format)
5. In Vercel, add:
   - **Key:** `DATABASE_URL`
   - **Value:** `postgresql://user:password@host:5432/dbname`

##### 2. Neon
1. Go to https://neon.tech
2. Create a new project
3. Copy the connection string
4. In Vercel, add:
   - **Key:** `DATABASE_URL`
   - **Value:** `postgresql://user:password@host:5432/dbname`

##### 3. Railway
1. Go to https://railway.app
2. Create a new project → Add PostgreSQL
3. Copy the connection string
4. In Vercel, add:
   - **Key:** `DATABASE_URL`
   - **Value:** `postgresql://user:password@host:5432/dbname`

## Step 3: Verify Environment Variables

Example environment setup:
```
SECRET_KEY=django-insecure-abcd1234...
DEBUG=False
ALLOWED_HOSTS=swapskill-pqw6yn3qt.vercel.app
DATABASE_URL=postgresql://user:password@db.example.com:5432/skillswap
```

## Step 4: Deploy

1. In Vercel Dashboard, go to **Deployments**
2. Click **"Redeploy"** on the latest build
3. Wait for the build to complete (usually 2-3 minutes)

During deployment, Vercel will:
- Install dependencies from `requirements.txt`
- Run migrations with `manage.py migrate`
- Collect static files with `manage.py collectstatic`
- Create a superuser (admin/admin123) if it doesn't exist

## Step 5: Access Your Application

Once deployment is complete:
1. Click the preview URL or go to your domain
2. You should see the SkillSwap homepage
3. Admin panel: `/admin/` (login with admin/admin123)

## Troubleshooting

### Error: "Python process exited with exit status: 1"
**Solution:** Check Vercel build logs for specific error messages:
1. Go to Deployments → Click failed deployment
2. Check "Runtime Logs" and "Build Logs"
3. Common issues:
   - Missing environment variables
   - Syntax errors in Python files
   - Database connection failed

### Error: "Static files not found (404)"
**Solution:** Ensure `python manage.py collectstatic` ran during build:
1. Check build logs
2. Verify `STATICFILES_STORAGE` is set to WhiteNoise
3. Check `STATIC_ROOT` and `STATIC_URL` in settings.py

### Error: "CSRF token missing"
**Solution:** Verify `ALLOWED_HOSTS` includes your exact Vercel domain:
```
ALLOWED_HOSTS=your-project-name.vercel.app
```

### Database Errors
**Solution:** Check DATABASE_URL connection string:
1. Verify the connection string format
2. Check database credentials
3. Ensure IP is whitelisted (for managed databases)

## Important Notes

### Local Development
For local development, the app uses SQLite:
```bash
# Local
python manage.py runserver
# Uses: db.sqlite3

# Vercel
# Uses: PostgreSQL (if DATABASE_URL set) or SQLite (in /tmp, not persistent)
```

### Data Persistence
- **SQLite on Vercel:** Data persists only during a single deployment. On redeployment, data is reset.
- **PostgreSQL:** Data persists across all deployments.

For production use, **always set up PostgreSQL**.

### Custom Domain
1. In Vercel, go to **Project Settings → Domains**
2. Add your custom domain
3. Update `ALLOWED_HOSTS` in environment variables to include your domain

## Build Commands

The following commands run during Vercel build (defined in `vercel-build.sh`):
```bash
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear
python manage.py shell  # Creates superuser if needed
```

## Files Modified for Vercel Deployment

- `api/wsgi.py` - WSGI application entry point
- `vercel.json` - Vercel build configuration
- `vercel-build.sh` - Build script
- `config/settings.py` - Django settings with environment variables
- `requirements.txt` - Python dependencies

## Getting Help

- Vercel Documentation: https://vercel.com/docs/frameworks/django
- Django Documentation: https://docs.djangoproject.com/
- Check GitHub Issues: https://github.com/CodeCraftSolution006/swapskill/issues

## Next Steps

1. ✅ Set up environment variables
2. ✅ Deploy to Vercel
3. ✅ Test the live application
4. ✅ (Optional) Set up custom domain
5. ✅ (Optional) Configure PostgreSQL for persistent data

---

**Your SkillSwap application is ready for production deployment!**
