# Quick Vercel Deployment Checklist

✅ **All files are ready. Here's what to do next:**

## Step 1: Go to Vercel Dashboard
1. Visit https://vercel.com
2. Sign in with GitHub (if not already)
3. Click **"Add New"** → **"Project"**

## Step 2: Import Repository
1. Select **"Import Git Repository"**
2. Find and select `CodeCraftSolution006/swapskill`
3. Click **"Import"**

## Step 3: Configure Environment Variables
Click **"Environment Variables"** and add these three variables:

### Required Variables:

**1. SECRET_KEY**
- Generate a secure key locally:
  ```powershell
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- Copy the output and paste it as the SECRET_KEY value
- Example: `django-insecure-a1b2c3d4e5f6g7h8i9j0...`

**2. DEBUG**
- Value: `False` (production mode)

**3. ALLOWED_HOSTS**
- Value: `your-project-name.vercel.app` (Vercel will give you this after first deploy)
- Or if you have a custom domain: `your-domain.com,your-project-name.vercel.app`

### Optional: DATABASE_URL (for Production Persistence)
If you want your data to persist in production (recommended), add:
- Key: `DATABASE_URL`
- Value: PostgreSQL connection string from Supabase, Render, or Railway
- Example: `postgresql://user:password@host:5432/dbname`

**Without this, SQLite will reset on each deploy!**

## Step 4: Framework & Build Settings
Vercel should auto-detect Python. Verify these settings:

- **Build Command:** 
  ```
  pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
  ```
- **Output Directory:** `.` (leave empty or set to root)
- **Install Command:** (leave as default, Vercel auto-detects)

## Step 5: Deploy!
1. Click **"Deploy"**
2. Wait for the build to complete (usually 2-3 minutes)
3. Once complete, you'll get a live URL like: `https://swapskill-xxxxx.vercel.app`

---

## Step 6: Test Register & Login

Visit your deployment URL and test:
1. **Register:** Create a new account
2. **Login:** Sign in with the account you just created
3. **Browse:** Check if pages load correctly

---

## Common Issues & Fixes

### ❌ "ModuleNotFoundError: No module named 'vercel_wsgi'"
**Fix:** Vercel will automatically install from `requirements.txt`. Check build logs for other errors.

### ❌ "Static files not loading (404 errors)"
**Cause:** collectstatic didn't run during build
**Fix:** Check Vercel build logs. Usually happens if database migration fails first.

### ❌ "Login not working"
**Possible causes:**
1. Database didn't initialize (migration failed)
2. `ALLOWED_HOSTS` doesn't include your Vercel domain
3. `SECRET_KEY` not set

**Debug:**
- Go to Vercel Dashboard → Project → Deployments
- Click the deployment → "View Logs"
- Look for error messages

### ❌ "CSRF token missing"
**Fix:** Ensure `ALLOWED_HOSTS` in environment variables includes your exact Vercel domain

### ❌ "Data disappears after redeploy"
**Cause:** Using SQLite without DATABASE_URL
**Fix:** Add PostgreSQL connection string to DATABASE_URL environment variable

---

## For Production: Add a Real Database

SQLite doesn't persist on Vercel. For production users, you MUST use PostgreSQL.

### Free PostgreSQL Options:
1. **Supabase** (most user-friendly): https://supabase.com
   - Free tier: 500MB storage, up to 10 connections
   - Get connection string from Settings → Database

2. **Render**: https://render.com
   - Free tier available
   - Get connection string from Instance Details

3. **Railway**: https://railway.app
   - $5/month free tier
   - Get connection string from Database

### Setup Steps:
1. Create PostgreSQL database with any provider
2. Get connection string (looks like: `postgresql://user:pass@host:5432/db`)
3. In Vercel dashboard, add environment variable `DATABASE_URL` = your connection string
4. Redeploy (git push origin main)

---

## Files Prepared for Vercel

```
✓ api/wsgi.py           → Django entrypoint for Vercel
✓ vercel.json           → Vercel configuration with build commands
✓ requirements.txt      → Python packages (vercel-wsgi, whitenoise, dj-database-url, etc.)
✓ config/settings.py    → Updated for production (env vars, WhiteNoise, PostgreSQL support)
✓ DEPLOYMENT.md         → Detailed deployment guide
✓ build.sh              → Build script (migrations + static files)
✓ .env.example          → Local development environment variables template
```

---

## Summary

**Your app is deployment-ready!**

1. ✅ Push to GitHub (already done)
2. ⏳ Connect to Vercel and set environment variables
3. ⏳ Deploy
4. ⏳ Test login/register
5. ✅ (Optional) Add PostgreSQL for data persistence

**Questions?** Check `DEPLOYMENT.md` for detailed troubleshooting and setup instructions.

**Ready to deploy?** https://vercel.com/import/project
