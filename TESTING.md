# SkillSwap - Testing & Example Data Guide

## 🧪 Manual Testing Guide

### Test Account Credentials
Create these accounts during testing:

**Admin Account (Superuser)**
```
Username: admin
Password: admin123!
Email: admin@skillswap.com
```

**Test Users**
```
User 1:
Username: john_doe
Password: TestPass123!
Email: john@example.com
First Name: John
Last Name: Doe

User 2:
Username: jane_smith
Password: TestPass123!
Email: jane@example.com
First Name: Jane
Last Name: Smith

User 3:
Username: alex_jones
Password: TestPass123!
Email: alex@example.com
First Name: Alex
Last Name: Jones
```

### Testing Checklist

#### 1. Authentication Testing
- [ ] Register new account
  - [ ] With valid email
  - [ ] With duplicate email (should fail)
  - [ ] With password mismatch (should fail)
  - [ ] With weak password (should fail)
- [ ] Login with correct credentials
- [ ] Login with wrong credentials (should fail)
- [ ] Logout functionality
- [ ] Session persistence
- [ ] Redirect after login to dashboard
- [ ] Redirect after logout to homepage

#### 2. Profile Management
- [ ] Create profile on registration
- [ ] Edit profile information
  - [ ] Update first name
  - [ ] Update last name
  - [ ] Update email
  - [ ] Update bio
  - [ ] Update location
  - [ ] Upload profile picture
- [ ] View own profile
- [ ] View other users' profiles
- [ ] Check user ratings
- [ ] Check user reviews

#### 3. Skill Management
- [ ] Add new skill
  - [ ] With all required fields
  - [ ] With optional image
  - [ ] Different categories (test all 10)
  - [ ] Different levels (test all 4)
- [ ] View skill details
- [ ] Edit existing skill
- [ ] Delete skill
- [ ] Image upload and display
- [ ] Skills appear on user profile
- [ ] Skills appear on dashboard

#### 4. Browsing & Searching
- [ ] Browse all skills page loads
- [ ] Search by skill name works
- [ ] Search by partial name works
- [ ] Filter by category works
- [ ] Filter by multiple categories
- [ ] Clear filters button
- [ ] Skill cards display correctly
- [ ] Pagination (if added)

#### 5. Skill Exchange
- [ ] Cannot exchange with self (should show error)
- [ ] Request exchange form shows own skills
- [ ] Submit exchange request with message
- [ ] Submit exchange request without message
- [ ] View pending requests on dashboard
- [ ] Accept exchange request
- [ ] Reject exchange request
- [ ] Exchange status updates correctly
- [ ] Cannot exchange with fewer than required skills

#### 6. Reviews & Ratings
- [ ] Mark exchange as complete
- [ ] Redirects to review page
- [ ] Submit review with rating
- [ ] Submit review with comment
- [ ] Review appears on user profile
- [ ] Rating calculation is correct
- [ ] Cannot review same user twice for same exchange
- [ ] User rating updates after review

#### 7. Admin Panel
- [ ] Login to admin panel
- [ ] View user profiles
- [ ] View all skills
- [ ] View skill exchanges
- [ ] View reviews
- [ ] Edit/delete users
- [ ] Edit/delete skills
- [ ] Filter by date
- [ ] Search functionality

#### 8. UI/UX Testing
- [ ] Navigation works on all pages
- [ ] Mobile responsiveness
- [ ] All buttons clickable
- [ ] Form validation messages
- [ ] Success/error messages display
- [ ] Images load correctly
- [ ] Links work properly
- [ ] No console errors

### Test Scenarios

#### Scenario 1: Complete Skill Exchange
1. Login as john_doe
2. Go to Dashboard → Add Skill
3. Add "Python Programming" skill
4. Logout and login as jane_smith
5. Go to Dashboard → Add Skill
6. Add "Spanish Language" skill
7. Click Browse Skills
8. Search for "Python"
9. Click View Details
10. Click Request Exchange
11. Select "Spanish Language"
12. Add message: "I want to learn Python"
13. Submit
14. Logout, login as john_doe
15. Go to Dashboard → Exchanges
16. Click Respond on pending request
17. Accept the exchange
18. Mark as complete
19. Leave a 5-star review for jane_smith
20. Verify rating updated on jane's profile

#### Scenario 2: Reject Exchange
1. Login as alex_jones
2. Add "Guitar Lessons" skill
3. Logout, login as john_doe
4. Browse skills and request exchange
5. Logout, login as alex_jones
6. Go to Dashboard → Exchanges
7. Reject the request
8. Verify status changed to "Rejected"

#### Scenario 3: User Profile Management
1. Register new account: "test_user"
2. Add profile picture
3. Update bio with some text
4. Update location
5. Visit profile page
6. Verify all information displays
7. Have another user visit your profile
8. Verify they can see your skills

### Performance Testing
- [ ] Page loads in < 2 seconds
- [ ] Image uploads are fast (< 5MB)
- [ ] Search response time acceptable
- [ ] No database errors in console
- [ ] No JavaScript errors in browser console

### Security Testing
- [ ] Cannot access other user's edit profile page
- [ ] Cannot edit other user's skills
- [ ] Cannot delete other user's skills
- [ ] Cannot modify exchange status manually
- [ ] CSRF token present on all forms
- [ ] SQL injection attempts fail
- [ ] XSS attacks blocked

## 📝 Creating Sample Data

### Using Django Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Create UserProfiles
4. Create Skills
5. Create SkillExchanges
6. Create Reviews

### Via Django Shell
```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from skillswap.models import UserProfile, Skill

# Create user
user = User.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpass123'
)

# Create profile
profile = UserProfile.objects.get(user=user)
profile.bio = 'I love programming!'
profile.location = 'New York'
profile.save()

# Create skill
skill = Skill.objects.create(
    owner=profile,
    name='Python Programming',
    description='Learn Python from basics to advanced',
    category='programming',
    level='advanced'
)

print(f"Created skill: {skill.name}")
```

## 🐛 Common Issues During Testing

### Issue: Static files not loading
**Solution:** Run `python manage.py collectstatic --noinput`

### Issue: Images not uploading
**Solution:** Ensure media directory exists: `mkdir media`

### Issue: Database locks
**Solution:** Delete db.sqlite3 and run `python manage.py migrate`

### Issue: Port 8000 in use
**Solution:** Run `python manage.py runserver 8080`

### Issue: Template not found
**Solution:** Verify templates are in `skillswap/templates/skillswap/`

## ✅ Final Verification

Before considering testing complete:
- [ ] All pages load without errors
- [ ] All CRUD operations work
- [ ] All forms validate properly
- [ ] Messages display correctly
- [ ] Exchange workflow complete
- [ ] Rating system functional
- [ ] Admin panel accessible
- [ ] No console errors
- [ ] Responsive on mobile
- [ ] Performance acceptable

---

**Last Updated:** 2025
**Status:** Ready for Testing
