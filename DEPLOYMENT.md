# Vercel Deployment Guide

## Overview
This Django project is configured to deploy on Vercel using serverless Python functions. Vercel will automatically install all dependencies from `requirements.txt`.

## Quick Deployment Steps

### 1. Ensure Code is Pushed to GitHub
```bash
git add .
git commit -m "Prepare for Vercel deployment"
git push -u origin main
```

### 2. Deploy to Vercel (UI Method)
1. Go to [vercel.com](https://vercel.com) and sign in
2. Click **"Add New Project"** → **"Import Git Repository"**
3. Select your GitHub repo (`CodeCraftSolution006/swapskill`)
4. **Vercel will automatically detect Python** and set Build Command to:
   ```
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```
5. Set **Output Directory** to `.` (root)
6. Click **"Environment Variables"** and add these (see section below):
   - `SECRET_KEY`
   - `DEBUG`
   - `ALLOWED_HOSTS`
7. Click **"Deploy"**

### 3. Environment Variables (Vercel Dashboard)

**Add these in Vercel Project Settings → Environment Variables:**

| Variable | Value | Example |
|----------|-------|---------|
| `SECRET_KEY` | A secure random string (use Django's secret key generator) | `django-insecure-abc123xyz...` |
| `DEBUG` | `False` (for production) | `False` |
| `ALLOWED_HOSTS` | Your Vercel domain and any custom domains | `your-project.vercel.app,yourdomain.com` |
| `DATABASE_URL` | (Optional) PostgreSQL connection string if using external DB | See below |

**To generate a secure SECRET_KEY locally:**
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. Database Configuration

#### Option A: SQLite (Simple, but NOT recommended for production)
- By default, the app uses SQLite (`db.sqlite3`)
- **Warning:** Vercel's ephemeral storage means SQLite will be lost after each deploy
- Only use for testing/demo purposes

#### Option B: PostgreSQL (Recommended for production)
Vercel will install `dj-database-url` (add to requirements.txt) and use `DATABASE_URL` environment variable.

**Steps:**
1. Provision a PostgreSQL database from one of these services:
   - [Supabase](https://supabase.com) (free tier available)
   - [Render](https://render.com) (free tier available)
   - [Railway](https://railway.app)
   - [Heroku Postgres](https://www.heroku.com/postgres)
   - [DigitalOcean](https://www.digitalocean.com/products/managed-databases)

2. Get your PostgreSQL connection string (looks like):
   ```
   postgresql://username:password@host:5432/dbname
   ```

3. In Vercel dashboard, add environment variable:
   - Key: `DATABASE_URL`
   - Value: Your PostgreSQL connection string

4. The app will automatically use PostgreSQL if `DATABASE_URL` is set.

### 5. Build & Deployment Flow

When you push to GitHub:
1. Vercel detects changes
2. Installs packages from `requirements.txt`
3. Runs migrations: `python manage.py migrate`
4. Collects static files: `python manage.py collectstatic --noinput`
5. Deploys the app

**Static files** are served using WhiteNoise middleware (already configured in `settings.py`).

---

## Testing Locally Before Deploying

### 1. Install Dependencies
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 2. Set Environment Variables (Locally)
```powershell
# In PowerShell:
$env:SECRET_KEY = "test-secret-key"
$env:DEBUG = "True"
$env:ALLOWED_HOSTS = "127.0.0.1,localhost"
```

### 3. Run Migrations
```powershell
python manage.py migrate
```

### 4. Collect Static Files
```powershell
python manage.py collectstatic --noinput
```

### 5. Run Development Server
```powershell
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and test:
- Register a new account
- Login
- Check all pages load

### 6. Test with Vercel CLI (Optional)
```powershell
npm install -g vercel
vercel dev
```

This simulates the Vercel production environment locally.

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'vercel_wsgi'"
**Fix:** Ensure `vercel-wsgi` is in `requirements.txt` and Vercel has rebuilt.

### Issue: Static files not loading (404)
**Fix:**
1. Ensure `python manage.py collectstatic --noinput` runs during build
2. Verify `STATICFILES_STORAGE` is set to `'whitenoise.storage.CompressedStaticFilesStorage'` in `settings.py`
3. Check that static files are in `skillswap/static/` directory

### Issue: Login/Register not working
**Possible causes:**
- Database migrations didn't run: Check Vercel build logs
- `SECRET_KEY` not set: Add it to Vercel Environment Variables
- `ALLOWED_HOSTS` doesn't include your Vercel domain

**Solution:**
1. Go to Vercel dashboard → Project → Deployments
2. Click the failed/current deployment
3. Check "Build Logs" for error messages
4. Fix issues and redeploy: `git push origin main`

### Issue: "CSRF token missing" or "CSRF verification failed"
**Fix:**
- Ensure `ALLOWED_HOSTS` in Environment Variables includes your Vercel domain (e.g., `your-project.vercel.app`)
- Verify `CSRF_TRUSTED_ORIGINS` is set correctly (can add to `settings.py` if needed)

### Issue: Can't connect to database
**If using PostgreSQL:**
- Verify `DATABASE_URL` is set in Vercel Environment Variables
- Ensure your PostgreSQL server is accessible from Vercel (not blocked by firewall)
- Test the connection string locally:
  ```powershell
  python -c "import dj_database_url; print(dj_database_url.config())"
  ```

---

## Vercel Build Configuration (vercel.json)

The `vercel.json` file routes all requests to the Django WSGI app:
```json
{
  "version": 2,
  "builds": [
    { "src": "requirements.txt", "use": "@vercel/python" },
    { "src": "api/wsgi.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "api/wsgi.py" }
  ]
}
```

---

## Summary

✅ **All files needed for Vercel are in place:**
- `requirements.txt` — Updated with deployment packages
- `config/settings.py` — Configured for production (environment variables, WhiteNoise)
- `api/wsgi.py` — Vercel entrypoint
- `vercel.json` — Vercel build & routing config

✅ **Next steps:**
1. Set environment variables in Vercel dashboard
2. Connect your GitHub repo to Vercel
3. Vercel will automatically install packages and deploy

✅ **After deployment:**
- Create a test user to verify register/login works
- Monitor Vercel logs for any errors

---

## Need Help?

- Vercel Docs: https://vercel.com/docs/frameworks/django
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/
- Reach out with specific error messages from Vercel build logs!
