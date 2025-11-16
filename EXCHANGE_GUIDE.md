# 📱 SkillSwap - Exchange Requests & Chat Guide

## 🔄 How Skill Exchange Works

### Step-by-Step Flow

```
1. User A: Browse Skills
   ↓
2. User A: Finds User B's Skill
   ↓
3. User A: Clicks "Request Exchange"
   ↓
4. User A: Selects their skill to offer
   ↓
5. User A: Adds optional message
   ↓
6. User A: Clicks "Send Exchange Request"
   ↓
7. ✅ REQUEST SENT
   ↓
8. User B: Gets notification (sees in Dashboard)
   ↓
9. User B: Goes to Dashboard → Exchanges Tab
   ↓
10. User B: Sees pending request with "Respond" button
   ↓
11. User B: Clicks "Respond"
   ↓
12. User B: Accepts or Rejects
   ↓
13. ✅ REQUEST STATUS UPDATES
```

---

## 📊 Dashboard - Exchanges Tab (THE MAIN PLACE)

### What You'll See:

The **Exchanges Tab** in your Dashboard shows:

| Column | Shows |
|--------|-------|
| **Offering** | The skill being offered to you |
| **Requesting** | The skill they want from you |
| **User** | Who sent the request |
| **Status** | pending/accepted/completed/rejected |
| **Actions** | Buttons to respond or mark complete |

### Status Meanings:

- 🟡 **Pending** → Waiting for receiver to respond
- 🟢 **Accepted** → Both agreed, ready to meet
- 🔵 **Completed** → Exchange done, ready for review
- 🔴 **Rejected** → One person rejected

---

## 💬 Message Feature

### Where to Send Messages

When you **Request Exchange**, you can add a message:

```
"Hi! I'd love to learn Python from you. 
I can teach you Spanish in return. 
Let's meet next week?"
```

This message appears when the other user:
1. Goes to Dashboard
2. Clicks "Exchanges" tab
3. Sees the request with your message

---

## 🔍 Finding Pending Requests

### YOUR Dashboard:

```
Dashboard
├── My Skills Tab
│   └── Your added skills
│
└── Exchanges Tab ← LOOK HERE
    ├── Pending Requests (waiting for others)
    ├── Accepted Requests (both agreed)
    ├── Completed Requests (ready to review)
    └── Rejected Requests (didn't work out)
```

### How to Check:

1. **Login** to your account
2. Click **Dashboard** in navigation
3. Click **"Exchanges"** tab (second tab)
4. You'll see a table with all exchanges

---

## 📋 Exchanges Table Columns

```
┌─────────────────┬──────────────────┬──────────┬────────────┬──────────────┐
│ Offering        │ Requesting       │ User     │ Status     │ Actions      │
├─────────────────┼──────────────────┼──────────┼────────────┼──────────────┤
│ Python Course   │ Spanish Lessons  │ john_doe │ Pending 🟡  │ Respond      │
│ Guitar Lessons  │ Photography      │ jane_sm  │ Accepted 🟢 │ Mark Complete│
│ Web Dev Bootcamp│ Cooking Class    │ alex_j   │ Completed 🔵│ Leave Review │
└─────────────────┴──────────────────┴──────────┴────────────┴──────────────┘
```

---

## 🎬 Complete Exchange Process

### Phase 1: REQUEST SENT 📤
**You:**
- Go to Browse Skills
- Find someone's skill
- Click "Request Exchange"
- Select your skill to offer
- Add message (optional)
- Click "Send Exchange Request"
- Status: "Pending"

**Them:**
- See it in Dashboard → Exchanges Tab
- See your message
- Two buttons: "Respond" or skip

---

### Phase 2: RESPONSE 📨
**Them (Receiver):**
- Click "Respond"
- See your skill vs their skill
- See your message
- Click "Accept" or "Reject"
- Status updates to: "Accepted" or "Rejected"

**You (Sender):**
- See updated status in Dashboard
- If accepted → Ready to meet!
- If rejected → See "Rejected" status

---

### Phase 3: MEET & EXCHANGE 🤝
**Both:**
- Exchange skills in real life or online
- No chat in app (arrange via message)
- Message stays visible for reference

---

### Phase 4: MARK COMPLETE ✅
**Either can click:**
- "Mark Complete" button
- Status changes to: "Completed"

---

### Phase 5: LEAVE REVIEW ⭐
**Both can:**
- Go back to Dashboard → Exchanges
- Click "Leave Review"
- Rate: 1-5 stars
- Add comment
- Submit
- Appears on user profile

---

## 🔔 Notifications

Currently, there's **NO real-time chat**, but you can see:

### In Dashboard → Exchanges Tab:
- ✅ All pending requests waiting for you
- ✅ Who sent it and when
- ✅ Their message to you
- ✅ Which skills are involved

### The Message You Receive:

When someone requests exchange, the message you sent appears here:

```
Exchange Request from: john_doe

They Offer: Python Programming
You Need: Spanish Lessons

Message from them:
"Hi! I'd love to learn Python from you. 
I can teach you Spanish in return. 
Let's meet next week?"

[Accept] [Reject]
```

---

## 📍 EXACT LOCATIONS

### To See Pending Requests:

```
URL: http://127.0.0.1:8000/dashboard/
      ↓
      [Dashboard]
      ↓
      Click "Exchanges" Tab
      ↓
      See Table with All Exchanges
      ↓
      Find ones with Status = "Pending"
      ↓
      Click "Respond" Button
```

### To Send a Request:

```
URL: http://127.0.0.1:8000/browse-skills/
      ↓
      Find a Skill You Like
      ↓
      Click "View Details"
      ↓
      Click "Request Exchange"
      ↓
      Select Your Skill
      ↓
      Add Message (optional)
      ↓
      Click "Send Exchange Request"
      ↓
      See confirmation
      ↓
      Status: Pending (in your Dashboard)
```

---

## ✨ Example Workflow

### You Want to Learn Python:

1. Go to **Browse Skills**
2. Search "Python" 
3. Find John's Python course
4. Click "View Details"
5. Click **"Request Exchange"**
6. See form asking:
   - "Select a skill to offer"
   - "Add a message"
7. You select "Spanish Lessons" you offer
8. You type: "Hi John! Can we exchange? I'll teach you Spanish and learn Python from you!"
9. Click **"Send Exchange Request"**
10. ✅ Request sent!

### John Receives It:

1. John logs in
2. Goes to **Dashboard**
3. Clicks **Exchanges** tab
4. Sees your request:
   - **Offering:** Spanish Lessons (from you)
   - **Requesting:** Python Programming (yours)
   - **Status:** Pending 🟡
   - **Message:** "Hi John! Can we exchange?..."
5. Has two options:
   - **Respond** → Accept or Reject
   - Do nothing → Stays pending

### John Accepts:

1. John clicks **"Respond"**
2. Sees both skills clearly
3. Sees your message
4. Clicks **"Accept Exchange"**
5. Status changes to: **Accepted** ✅

### Both See Updated Status:

1. You check Dashboard → Exchanges
2. See: "Accepted" status
3. Ready to meet!

### After Meeting:

1. Either clicks: **"Mark Complete"**
2. Status: **"Completed"**
3. Redirected to **leave review**
4. Rate John: ⭐⭐⭐⭐⭐ (5 stars)
5. Add comment: "Great teacher! Very patient!"
6. Submit
7. Review appears on John's profile

---

## 🎯 Testing This Now

### Test Exchange:

1. **Create 2 accounts:**
   - Account 1: john_doe (Add Python skill)
   - Account 2: jane_smith (Add Spanish skill)

2. **Login as jane_smith**
   - Go to Browse Skills
   - Find john_doe's Python
   - Click "Request Exchange"
   - Select "Spanish Lessons"
   - Add message
   - Click "Send"

3. **Login as john_doe**
   - Go to Dashboard
   - Click Exchanges tab
   - See jane_smith's request
   - See her message
   - Click "Respond"
   - Accept

4. **Back to jane_smith**
   - Refresh Dashboard
   - See "Accepted" status

5. **Both complete:**
   - Either clicks "Mark Complete"
   - Leave review with rating

---

## 📝 Summary

| Question | Answer |
|----------|--------|
| Where are pending requests? | Dashboard → Exchanges Tab |
| How do I respond? | Click "Respond" button in exchanges table |
| Where's the chat? | Message appears in the request exchange form |
| How do they know I sent request? | They see it in their Dashboard Exchanges tab |
| Can we message after? | Message stays visible in exchange details |
| How to complete? | Click "Mark Complete" when done meeting |
| How to review? | Click "Leave Review" after completed |

---

## 🚀 Quick Links

- **Dashboard:** http://127.0.0.1:8000/dashboard/
- **Browse Skills:** http://127.0.0.1:8000/browse-skills/
- **My Profile:** http://127.0.0.1:8000/profile/USERNAME/

---

**Happy exchanging! 🎉**
