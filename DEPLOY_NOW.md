# 🚀 Deploy SkillSwap to Vercel - Complete Guide

## Current Status ✅
- Project is ready for Vercel deployment
- All code is committed to GitHub (`main` branch)
- Database configured to support both SQLite (local) and PostgreSQL (production)
- Build scripts prepared

## Database Configuration

### Local Development
- **Database:** SQLite (`db.sqlite3`)
- **Command:** `python manage.py runserver`
- **Data Persistence:** Permanent (stored in project folder)

### Vercel Deployment Options

#### Option 1: SQLite (Default - No Setup)
- **Pros:** No setup required, works immediately
- **Cons:** Data resets on redeploy, not suitable for production
- **Best for:** Testing/staging only

#### Option 2: PostgreSQL (Recommended)
- **Pros:** Persistent data, production-ready, free tier available
- **Cons:** Requires 5 minutes to set up
- **Best for:** Production use

## Step-by-Step Deployment

### Phase 1: Prepare Environment Variables

#### 1. Generate SECRET_KEY
Open terminal and run:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output - you'll need it in Vercel.

#### 2. Gather Required Information
You'll need these three things:
1. **SECRET_KEY** - From step above (example: `django-insecure-abc123xyz...`)
2. **ALLOWED_HOSTS** - Will be provided by Vercel after first deploy (example: `skillswap-abc123.vercel.app`)
3. **DATABASE_URL** - Only if using PostgreSQL (optional, skip if using SQLite)

### Phase 2: Deploy to Vercel

#### Method A: Via Vercel Dashboard (Recommended)

1. **Go to Vercel Dashboard**
   - Visit https://vercel.com/dashboard
   - Make sure you're signed in

2. **Import Project**
   - Click **"Add New"** button
   - Select **"Project"**
   - Click **"Import Git Repository"**
   - Search for `swapskill` repository
   - Click **"Import"**

3. **Review Project Settings**
   - Framework: Django (auto-detected)
   - Build Command: Auto-detected
   - Click **"Deploy"**

Vercel will start building. Wait 2-3 minutes...

#### Method B: Via CLI

```bash
# Install Vercel CLI globally
npm install -g vercel

# Login to Vercel
vercel login

# Deploy in production mode
cd d:\Collaborating with MT\skillswap_project\skillswap_project
vercel --prod
```

### Phase 3: Configure Environment Variables

After initial deployment (or before redeployment):

1. **Go to Vercel Project Settings**
   - Dashboard → Select your project
   - Go to **"Settings"** tab
   - Click **"Environment Variables"** (left sidebar)

2. **Add Variables**
   - Click **"Add New Variable"**
   - For each variable below, enter Key and Value, then click "Save"

**Required Variables:**

| Key | Value | Example |
|-----|-------|---------|
| `SECRET_KEY` | Your generated key from Phase 1 | `django-insecure-a1b2c3d4e5f6g7h8i9j0...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | Your Vercel domain | `skillswap-abc123def.vercel.app` |

**Optional Variables (for PostgreSQL):**

| Key | Value | Example |
|-----|-------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@db.supabase.com:5432/postgres` |

### Phase 4: Set Up Database (PostgreSQL - Optional)

If you want persistent data across redeploys:

#### Option A: Supabase (Easiest)
1. Go to https://supabase.com
2. Sign up and create a new project
3. Go to **Settings → Database → Connection String**
4. Copy the URI format connection string
5. Replace `[YOUR-PASSWORD]` with your actual password
6. Add to Vercel as `DATABASE_URL` environment variable
7. Redeploy in Vercel

#### Option B: Neon
1. Go to https://neon.tech
2. Create account and project
3. Copy the connection string from dashboard
4. Add to Vercel as `DATABASE_URL`
5. Redeploy in Vercel

#### Option C: Railway
1. Go to https://railway.app
2. Create project → Add PostgreSQL
3. Copy connection string
4. Add to Vercel as `DATABASE_URL`
5. Redeploy in Vercel

### Phase 5: Redeploy with Environment Variables

After adding environment variables:

1. **Go to Deployments**
   - Dashboard → Select your project
   - Click **"Deployments"** tab

2. **Redeploy**
   - Find the latest deployment
   - Click the three dots **"..."** menu
   - Select **"Redeploy"**
   - Click **"Redeploy"** again to confirm

Vercel will redeploy with your environment variables. Wait 2-3 minutes...

### Phase 6: Verify Deployment

Once deployment completes:

1. **Access Your Application**
   - Vercel will show your URL (example: `https://skillswap-abc123.vercel.app`)
   - Click the URL to visit your live application

2. **Test Key Features**
   - Homepage loads correctly
   - Navigation bar works
   - Click "Browse Skills" - should show skills
   - Click "Register" - form appears
   - Try logging in with admin/admin123 (default credentials)
   - Visit `/admin/` - admin panel should work

3. **Check Admin Panel**
   - Go to `https://your-domain.vercel.app/admin/`
   - Login with: **admin** / **admin123**
   - View Users, Skills, and Exchanges

### Phase 7: Monitor and Troubleshoot

**Check Logs if Issues Occur:**
1. Go to your Vercel project
2. Click **"Deployments"** → Click failed deployment
3. View **"Runtime Logs"** and **"Build Logs"**

**Common Issues and Fixes:**

| Problem | Solution |
|---------|----------|
| Page shows 500 error | Check Runtime Logs for Python errors |
| "Process exited with status 1" | Verify all env vars are set correctly |
| Static files not loading | Check that `collectstatic` ran in build logs |
| CSRF token errors | Update ALLOWED_HOSTS to include exact domain |
| Can't connect to database | Verify DATABASE_URL connection string is correct |

## Environment Variables Reference

### For Local Development
Create a `.env` file in project root:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### For Vercel Production
Set these in Vercel Dashboard:
```
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-project.vercel.app
DATABASE_URL=postgresql://user:password@host/dbname  # Optional
```

## Build Process

During Vercel deployment, these commands run automatically:
```bash
pip install -r requirements.txt          # Install Python packages
python manage.py migrate                 # Run database migrations
python manage.py collectstatic --noinput # Collect static files
```

## Data Persistence Summary

| Storage Type | Local Dev | Vercel with SQLite | Vercel with PostgreSQL |
|--------------|-----------|-------------------|----------------------|
| Data persists after redeploy | ✅ Yes | ❌ No | ✅ Yes |
| Setup required | None | None | 5 min (PostgreSQL) |
| Production-ready | No | No | ✅ Yes |
| Cost | Free | Free | Free (initial) |

**Recommendation:** Use PostgreSQL for any production deployment.

## Next Steps

After successful deployment:

1. **Share your live URL:**
   - Copy from Vercel dashboard
   - Share with team or users
   - Example: `https://skillswap-abc123def.vercel.app`

2. **Set up custom domain (optional):**
   - In Vercel: Settings → Domains
   - Add your custom domain
   - Update ALLOWED_HOSTS in Vercel

3. **Enable database backups (if using PostgreSQL):**
   - Depends on your database provider
   - Supabase has automatic backups
   - Check your provider's documentation

4. **Monitor application:**
   - Check Vercel analytics
   - Monitor error rates
   - Set up notifications for failures

## Support

If you encounter issues:
1. Check build logs in Vercel
2. Review error messages carefully
3. Verify all environment variables are set
4. Check GitHub issues for similar problems
5. Test locally first before deploying

## Files Related to Deployment

- `vercel.json` - Vercel configuration
- `vercel-build.sh` - Build script
- `config/settings.py` - Django settings (loads env vars)
- `requirements.txt` - Python dependencies
- `api/wsgi.py` - WSGI entry point

## Deployment Timeline

- **Setup time:** 5 minutes (just env vars)
- **Deployment time:** 2-3 minutes
- **Total time:** 7-10 minutes
- **Database setup (PostgreSQL):** Additional 5 minutes (optional)

---

## ✅ Checklist for Final Deployment

- [ ] Generated SECRET_KEY
- [ ] Have Vercel account
- [ ] Repository pushed to GitHub main branch
- [ ] Imported project to Vercel
- [ ] Set environment variables:
  - [ ] SECRET_KEY
  - [ ] DEBUG=False
  - [ ] ALLOWED_HOSTS=<your-vercel-domain>
- [ ] (Optional) Set up PostgreSQL DATABASE_URL
- [ ] Redeployed with environment variables
- [ ] Verified application loads
- [ ] Tested key features
- [ ] Admin panel works
- [ ] Live URL shared

---

**🎉 Your SkillSwap application is now live on Vercel!**

For detailed information, see:
- `DEPLOYMENT_CHECKLIST.md` - Quick checklist
- `VERCEL_DEPLOYMENT.md` - Detailed deployment guide
