# ⚡ Quick Vercel Deployment Checklist

## Pre-Deployment (5 minutes)

- [ ] All code is pushed to GitHub main branch
- [ ] No uncommitted changes locally
- [ ] Run `python manage.py test` locally to verify everything works

## Vercel Setup (2 minutes)

- [ ] Have Vercel account ready (https://vercel.com)
- [ ] Have GitHub connected to Vercel
- [ ] Repository is public on GitHub

## Environment Variables Setup (3 minutes)

Generate required values:

### 1. SECRET_KEY
```bash
# Copy this command output
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 2. Set These in Vercel Dashboard (Project Settings → Environment Variables)

| Key | Value | Example |
|-----|-------|---------|
| `SECRET_KEY` | From above | `django-insecure-a1b2c3d4...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | Your domain | `skillswap-pqw6yn3qt.vercel.app` |
| `DATABASE_URL` | *(Optional)* PostgreSQL connection | `postgresql://user:pass@host/db` |

## Deploy Steps (1 minute)

1. Go to https://vercel.com/dashboard
2. Click **"Add New"** → **"Project"**
3. Select **"Import Git Repository"**
4. Find `swapskill` repository
5. Click **"Import"**
6. Vercel will auto-detect Django configuration
7. Click **"Deploy"**

**OR** use CLI:
```bash
vercel --prod
```

## Post-Deployment (2 minutes)

- [ ] Deployment successful - check build logs
- [ ] Access live URL
- [ ] Test homepage loads
- [ ] Test login/register
- [ ] Check admin panel at `/admin/`
- [ ] Test a key feature (browse skills, create skill, etc.)

## Database Setup (Optional - 5 minutes for PostgreSQL)

If using local SQLite:
- Data will reset on redeploy (not recommended for production)

If using PostgreSQL (recommended):

1. **Choose a provider:**
   - Supabase (https://supabase.com)
   - Neon (https://neon.tech)
   - Railway (https://railway.app)

2. **Create database and get connection string**

3. **Add to Vercel environment variables:**
   ```
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

4. **Redeploy in Vercel**

## Verification

After deployment, verify:
- [ ] Homepage displays correctly
- [ ] Navigation works
- [ ] Can register new account
- [ ] Can login
- [ ] Can browse skills
- [ ] Can view profile
- [ ] Static files load (CSS/JS)
- [ ] Admin panel accessible

## Monitoring

After deploy, monitor:
1. Vercel Dashboard → Runtime Logs
2. Check for any Python errors
3. Watch for 500 errors

## Rollback

If something goes wrong:
1. Go to Vercel Deployments
2. Click previous deployment
3. Click "Redeploy"

## Common Issues & Quick Fixes

| Issue | Fix |
|-------|-----|
| 500 Error | Check Runtime Logs → look for Python errors |
| Static files 404 | Ensure `collectstatic` ran (check build logs) |
| CSRF errors | Update `ALLOWED_HOSTS` with correct domain |
| Database errors | Check `DATABASE_URL` connection string |
| "Process exited" | Check all environment variables are set |

---

**Estimated total time: 15-20 minutes**

**Need help?** See VERCEL_DEPLOYMENT.md for detailed guide
