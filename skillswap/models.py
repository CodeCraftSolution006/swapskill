from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('languages', 'Languages'),
        ('design', 'Design'),
        ('business', 'Business'),
        ('music', 'Music'),
        ('sports', 'Sports'),
        ('cooking', 'Cooking'),
        ('art', 'Art'),
        ('fitness', 'Fitness'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='skill_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.owner.user.username}"

    class Meta:
        ordering = ['-created_at']


class SkillExchange(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    skill_offered = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='exchanges_offered')
    skill_requested = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='exchanges_requested')
    requester = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='exchanges_requested')
    provider = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='exchanges_provided')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill_offered.name} <-> {self.skill_requested.name}"

    class Meta:
        ordering = ['-created_at']


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='messages_received')
    exchange = models.ForeignKey(SkillExchange, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.user.username} -> {self.receiver.user.username}: {self.content[:50]}"

    class Meta:
        ordering = ['created_at']


class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_given')
    reviewee = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    exchange = models.ForeignKey(SkillExchange, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.user.username} -> {self.reviewee.user.username}: {self.rating}/5"

    class Meta:
        ordering = ['-created_at']
        unique_together = ('reviewer', 'reviewee', 'exchange')
