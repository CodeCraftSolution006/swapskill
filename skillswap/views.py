from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import UserProfile, Skill, SkillExchange, Review, Message
from .forms import (UserRegistrationForm, UserProfileForm, UserUpdateForm, 
                    SkillForm, SkillExchangeForm, ReviewForm, MessageForm)


def index(request):
    """Home page"""
    skills = Skill.objects.all()[:6]
    total_users = UserProfile.objects.count()
    total_skills = Skill.objects.count()
    context = {
        'skills': skills,
        'total_users': total_users,
        'total_skills': total_skills,
    }
    return render(request, 'skillswap/index.html', context)


def register(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'skillswap/register.html', {'form': form})


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'skillswap/login.html')


@login_required
def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


@login_required
def dashboard(request):
    """User dashboard"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    skills = profile.skills.all()
    exchanges = SkillExchange.objects.filter(
        Q(requester=profile) | Q(provider=profile)
    ).order_by('-created_at')
    
    # Statistics
    completed_exchanges = exchanges.filter(status='completed').count()
    pending_exchanges = exchanges.filter(status='pending').count()
    average_rating = profile.reviews_received.aggregate(Avg('rating'))['rating__avg'] or 0
    
    # Unread messages
    unread_messages = Message.objects.filter(receiver=profile, is_read=False).count()
    
    # Admin statistics (only for admin user)
    is_admin = request.user.is_staff and request.user.is_superuser
    admin_stats = {}
    if is_admin:
        admin_stats = {
            'total_users': UserProfile.objects.count(),
            'total_skills': Skill.objects.count(),
            'total_exchanges': SkillExchange.objects.count(),
            'pending_exchanges': SkillExchange.objects.filter(status='pending').count(),
            'completed_exchanges': SkillExchange.objects.filter(status='completed').count(),
            'total_messages': Message.objects.count(),
            'unread_messages': Message.objects.filter(is_read=False).count(),
            'total_reviews': Review.objects.count(),
            'all_users': UserProfile.objects.all(),
            'all_skills': Skill.objects.all()[:10],
            'all_exchanges': SkillExchange.objects.all()[:10],
            'all_messages': Message.objects.all()[:10],
        }
    
    context = {
        'profile': profile,
        'skills': skills,
        'exchanges': exchanges,
        'completed_exchanges': completed_exchanges,
        'pending_exchanges': pending_exchanges,
        'average_rating': round(average_rating, 1),
        'unread_messages': unread_messages,
        'is_admin': is_admin,
        'admin_stats': admin_stats,

    }
    return render(request, 'skillswap/dashboard.html', context)


@login_required
def profile_edit(request):
    """Edit user profile"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', username=request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'skillswap/profile_edit.html', context)


def profile_view(request, username):
    """View user profile"""
    user = get_object_or_404(UserProfile, user__username=username)
    skills = user.skills.all()
    reviews = user.reviews_received.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    
    context = {
        'profile': user,
        'skills': skills,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),
        'total_reviews': reviews.count(),
    }
    return render(request, 'skillswap/profile.html', context)


@login_required
def skill_create(request):
    """Create a new skill"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill created successfully!')
            return redirect('dashboard')
    else:
        form = SkillForm()
    
    return render(request, 'skillswap/skill_form.html', {'form': form, 'action': 'Create'})


@login_required
def skill_edit(request, pk):
    """Edit a skill"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    skill = get_object_or_404(Skill, pk=pk, owner=profile)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully!')
            return redirect('dashboard')
    else:
        form = SkillForm(instance=skill)
    
    return render(request, 'skillswap/skill_form.html', {'form': form, 'action': 'Edit'})


@login_required
def skill_delete(request, pk):
    """Delete a skill"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    skill = get_object_or_404(Skill, pk=pk, owner=profile)
    
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'skillswap/skill_confirm_delete.html', {'skill': skill})


def skill_detail(request, pk):
    """View skill details"""
    skill = get_object_or_404(Skill, pk=pk)
    context = {'skill': skill}
    return render(request, 'skillswap/skill_detail.html', context)


def browse_skills(request):
    """Browse all skills"""
    skills = Skill.objects.all()
    
    # Filter by category
    category = request.GET.get('category', '')
    if category:
        skills = skills.filter(category=category)
    
    # Search
    search = request.GET.get('search', '')
    if search:
        skills = skills.filter(
            Q(name__icontains=search) | Q(description__icontains=search)
        )
    
    context = {
        'skills': skills,
        'current_category': category,
        'search_query': search,
    }
    return render(request, 'skillswap/browse_skills.html', context)


@login_required
def skill_exchange_request(request, skill_id):
    """Request a skill exchange"""
    # Get or create profile for user
    requester_profile, created = UserProfile.objects.get_or_create(user=request.user)
    skill = get_object_or_404(Skill, pk=skill_id)
    
    # Cannot exchange with yourself
    if skill.owner == requester_profile:
        messages.error(request, 'You cannot exchange with yourself.')
        return redirect('skill_detail', pk=skill_id)
    
    if request.method == 'POST':
        # Get the requester's skill
        requester_skill_id = request.POST.get('my_skill')
        requester_skill = get_object_or_404(Skill, pk=requester_skill_id, owner=requester_profile)
        
        form = SkillExchangeForm(request.POST)
        if form.is_valid():
            exchange = form.save(commit=False)
            exchange.skill_offered = skill
            exchange.skill_requested = requester_skill
            exchange.requester = requester_profile
            exchange.provider = skill.owner
            exchange.save()
            messages.success(request, 'Exchange request sent successfully!')
            return redirect('dashboard')
    else:
        form = SkillExchangeForm()
    
    requester_skills = requester_profile.skills.all()
    context = {
        'skill': skill,
        'form': form,
        'requester_skills': requester_skills,
    }
    return render(request, 'skillswap/exchange_request.html', context)


@login_required
def exchange_respond(request, exchange_id):
    """Respond to exchange request"""
    exchange = get_object_or_404(SkillExchange, pk=exchange_id)
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Only provider can respond
    if exchange.provider != profile:
        messages.error(request, 'You are not authorized to respond to this request.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            exchange.status = 'accepted'
            exchange.save()
            messages.success(request, 'Exchange accepted!')
        elif action == 'reject':
            exchange.status = 'rejected'
            exchange.save()
            messages.success(request, 'Exchange rejected.')
        
        return redirect('dashboard')
    
    return render(request, 'skillswap/exchange_respond.html', {'exchange': exchange})


@login_required
def exchange_complete(request, exchange_id):
    """Mark exchange as completed"""
    exchange = get_object_or_404(SkillExchange, pk=exchange_id)
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Either requester or provider can complete
    if exchange.requester != profile and exchange.provider != profile:
        messages.error(request, 'You are not part of this exchange.')
        return redirect('dashboard')
    
    if exchange.status != 'accepted':
        messages.error(request, 'Exchange must be accepted first.')
        return redirect('dashboard')
    
    exchange.status = 'completed'
    exchange.save()
    messages.success(request, 'Exchange completed!')
    
    # Redirect to review page
    return redirect('create_review', exchange_id=exchange.id)


@login_required
def create_review(request, exchange_id):
    """Create a review for completed exchange"""
    exchange = get_object_or_404(SkillExchange, pk=exchange_id)
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Determine reviewee
    if exchange.requester == profile:
        reviewee = exchange.provider
    elif exchange.provider == profile:
        reviewee = exchange.requester
    else:
        messages.error(request, 'You are not part of this exchange.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = profile
            review.reviewee = reviewee
            review.exchange = exchange
            review.save()
            
            # Update reviewer rating
            avg_rating = reviewee.reviews_received.aggregate(Avg('rating'))['rating__avg']
            reviewee.rating = avg_rating
            reviewee.save()
            
            messages.success(request, 'Review submitted successfully!')
            return redirect('profile', username=reviewee.user.username)
    else:
        # Check if review already exists
        existing_review = Review.objects.filter(
            reviewer=profile, 
            reviewee=reviewee, 
            exchange=exchange
        ).first()
        if existing_review:
            messages.info(request, 'You have already reviewed this user.')
            return redirect('profile', username=reviewee.user.username)
        
        form = ReviewForm()
    
    context = {
        'form': form,
        'exchange': exchange,
        'reviewee': reviewee,
    }
    return render(request, 'skillswap/review_form.html', context)


@login_required
def messages_list(request):
    """View all conversations"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Get all conversations (people who messaged or were messaged)
    sent_messages = Message.objects.filter(sender=profile).values('receiver').distinct()
    received_messages = Message.objects.filter(receiver=profile).values('sender').distinct()
    
    senders = UserProfile.objects.filter(id__in=[m['receiver'] for m in sent_messages])
    receivers = UserProfile.objects.filter(id__in=[m['sender'] for m in received_messages])
    
    conversations = list(senders) + list(receivers)
    # Remove duplicates while preserving order
    seen = set()
    unique_conversations = []
    for conv in conversations:
        if conv.id not in seen:
            seen.add(conv.id)
            unique_conversations.append(conv)
    
    context = {
        'conversations': unique_conversations,
    }
    return render(request, 'skillswap/messages_list.html', context)


@login_required
def chat_view(request, username):
    """View chat with specific user"""
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    other_user = get_object_or_404(UserProfile, user__username=username)
    
    # Prevent chat with self
    if other_user == profile:
        messages.error(request, 'You cannot message yourself.')
        return redirect('messages_list')
    
    # Get all messages between these two users
    conversation = Message.objects.filter(
        Q(sender=profile, receiver=other_user) |
        Q(sender=other_user, receiver=profile)
    ).order_by('created_at')
    
    # Mark received messages as read
    Message.objects.filter(sender=other_user, receiver=profile, is_read=False).update(is_read=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = profile
            message.receiver = other_user
            message.save()
            return redirect('chat_view', username=username)
    else:
        form = MessageForm()
    
    context = {
        'other_user': other_user,
        'conversation': conversation,
        'form': form,
    }
    return render(request, 'skillswap/chat.html', context)


@login_required
def exchange_chat_view(request, exchange_id):
    """Chat for specific exchange"""
    exchange = get_object_or_404(SkillExchange, pk=exchange_id)
    # Get or create profile for user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    # Determine the other user
    if exchange.requester == profile:
        other_user = exchange.provider
    elif exchange.provider == profile:
        other_user = exchange.requester
    else:
        messages.error(request, 'You are not part of this exchange.')
        return redirect('dashboard')
    
    # Get all messages between these two users
    conversation = Message.objects.filter(
        Q(sender=profile, receiver=other_user) |
        Q(sender=other_user, receiver=profile)
    ).order_by('created_at')
    
    # Mark received messages as read
    Message.objects.filter(sender=other_user, receiver=profile, is_read=False).update(is_read=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = profile
            message.receiver = other_user
            message.exchange = exchange
            message.save()
            return redirect('exchange_chat', exchange_id=exchange_id)
    else:
        form = MessageForm()
    
    context = {
        'other_user': other_user,
        'conversation': conversation,
        'form': form,
        'exchange': exchange,
    }
    return render(request, 'skillswap/chat.html', context)


@login_required
def unread_messages_count(request):
    """Get count of unread messages (for header badge)"""
    profile = request.user.userprofile
    count = Message.objects.filter(receiver=profile, is_read=False).count()
    return {'unread_count': count}
