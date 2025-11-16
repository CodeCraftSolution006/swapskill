from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile, Skill, SkillExchange, Review, Message

# ============================================================================
# USER PROFILE ADMIN
# ============================================================================

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username_display', 'email_display', 'rating_display', 'skills_count', 'exchanges_count', 'created_at')
    list_filter = ('created_at', 'rating')
    search_fields = ('user__username', 'user__email', 'bio')
    readonly_fields = ('rating', 'created_at', 'user_info', 'statistics')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'user_info')
        }),
        ('Profile Details', {
            'fields': ('bio', 'location', 'profile_picture')
        }),
        ('Rating', {
            'fields': ('rating',)
        }),
        ('Statistics', {
            'fields': ('statistics',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def username_display(self, obj):
        return format_html('<strong>{}</strong>', obj.user.username)
    username_display.short_description = 'Username'
    
    def email_display(self, obj):
        return obj.user.email
    email_display.short_description = 'Email'
    
    def rating_display(self, obj):
        if obj.rating:
            color = 'green' if obj.rating >= 4 else 'orange' if obj.rating >= 3 else 'red'
            return format_html(
                '<span style="color: {}; font-weight: bold;">{:.1f}★</span>',
                color, obj.rating
            )
        return format_html('<span style="color: gray;">No rating</span>')
    rating_display.short_description = 'Rating'
    
    def skills_count(self, obj):
        count = obj.skills.count()
        return format_html('<span style="background-color: #e7f3ff; padding: 3px 8px; border-radius: 3px;">{}</span>', count)
    skills_count.short_description = 'Skills'
    
    def exchanges_count(self, obj):
        count = obj.skillexchange_set.all().count()
        return format_html('<span style="background-color: #fff3e0; padding: 3px 8px; border-radius: 3px;">{}</span>', count)
    exchanges_count.short_description = 'Exchanges'
    
    def user_info(self, obj):
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;"><strong>Username:</strong> {}<br><strong>Email:</strong> {}<br><strong>Joined:</strong> {}</div>',
            obj.user.username, obj.user.email, obj.user.date_joined.strftime('%Y-%m-%d %H:%M')
        )
    user_info.short_description = 'User Information'
    
    def statistics(self, obj):
        completed = SkillExchange.objects.filter(status='completed').filter(
            skillexchange_id__in=[obj.skillexchange_set.all()]
        ).count()
        pending = obj.skillexchange_set.filter(status='pending').count()
        accepted = obj.skillexchange_set.filter(status='accepted').count()
        
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Pending:</strong> {}<br>'
            '<strong>Accepted:</strong> {}<br>'
            '<strong>Messages Sent:</strong> {}<br>'
            '<strong>Messages Received:</strong> {}'
            '</div>',
            pending, accepted,
            obj.messages_sent.count(), obj.messages_received.count()
        )
    statistics.short_description = 'Statistics'

# ============================================================================
# SKILL ADMIN
# ============================================================================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name_display', 'owner_display', 'category_display', 'level_display', 'created_at', 'actions_display')
    list_filter = ('category', 'level', 'created_at')
    search_fields = ('name', 'description', 'owner__user__username')
    readonly_fields = ('created_at', 'skill_info', 'exchange_count')
    
    fieldsets = (
        ('Skill Details', {
            'fields': ('name', 'description', 'category', 'level', 'image', 'owner')
        }),
        ('Additional Info', {
            'fields': ('skill_info', 'exchange_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def name_display(self, obj):
        return format_html('<strong>{}</strong>', obj.name)
    name_display.short_description = 'Skill Name'
    
    def owner_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.owner.id, obj.owner.user.username)
    owner_display.short_description = 'Owner'
    
    def category_display(self, obj):
        return format_html('<span style="background-color: #e7f3ff; padding: 3px 8px; border-radius: 3px;">{}</span>', 
                          obj.get_category_display())
    category_display.short_description = 'Category'
    
    def level_display(self, obj):
        colors = {'beginner': '#d4edda', 'intermediate': '#fff3cd', 'advanced': '#f8d7da', 'expert': '#cce5ff'}
        color = colors.get(obj.level, '#e2e3e5')
        return format_html('<span style="background-color: {}; padding: 3px 8px; border-radius: 3px;">{}</span>', 
                          color, obj.get_level_display())
    level_display.short_description = 'Level'
    
    def exchange_count(self, obj):
        offered_count = SkillExchange.objects.filter(skill_offered=obj).count()
        requested_count = SkillExchange.objects.filter(skill_requested=obj).count()
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Offered In:</strong> {} exchanges<br>'
            '<strong>Requested In:</strong> {} exchanges'
            '</div>',
            offered_count, requested_count
        )
    exchange_count.short_description = 'Exchange Count'
    
    def skill_info(self, obj):
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Description:</strong> {}<br><strong>Owner Rating:</strong> {}'
            '</div>',
            obj.description[:100] + '...' if len(obj.description) > 100 else obj.description,
            f"{obj.owner.rating:.1f}★" if obj.owner.rating else "No rating"
        )
    skill_info.short_description = 'Skill Info'
    
    def actions_display(self, obj):
        return format_html('<a class="button" href="/admin/skillswap/skill/{}/change/">Edit</a>', obj.id)
    actions_display.short_description = 'Actions'

# ============================================================================
# SKILL EXCHANGE ADMIN
# ============================================================================

@admin.register(SkillExchange)
class SkillExchangeAdmin(admin.ModelAdmin):
    list_display = ('exchange_id_display', 'requester_display', 'provider_display', 'skills_display', 'status_display', 'created_at', 'days_ago')
    list_filter = ('status', 'created_at')
    search_fields = ('requester__user__username', 'provider__user__username', 'skill_offered__name', 'skill_requested__name')
    readonly_fields = ('created_at', 'exchange_details', 'messages_count')
    
    fieldsets = (
        ('Exchange Details', {
            'fields': ('requester', 'provider', 'skill_offered', 'skill_requested', 'status', 'message')
        }),
        ('Additional Info', {
            'fields': ('exchange_details', 'messages_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def exchange_id_display(self, obj):
        return format_html('<strong>#{}</strong>', obj.id)
    exchange_id_display.short_description = 'ID'
    
    def requester_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.requester.id, obj.requester.user.username)
    requester_display.short_description = 'Requester'
    
    def provider_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.provider.id, obj.provider.user.username)
    provider_display.short_description = 'Provider'
    
    def skills_display(self, obj):
        return format_html(
            '<div><strong>Offered:</strong> {}<br><strong>Requested:</strong> {}</div>',
            obj.skill_offered.name, obj.skill_requested.name
        )
    skills_display.short_description = 'Skills'
    
    def status_display(self, obj):
        colors = {'pending': '#fff3cd', 'accepted': '#cce5ff', 'completed': '#d4edda', 'rejected': '#f8d7da'}
        color = colors.get(obj.status, '#e2e3e5')
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px; font-weight: bold;">{}</span>',
            color, obj.get_status_display()
        )
    status_display.short_description = 'Status'
    
    def days_ago(self, obj):
        from datetime import timedelta
        from django.utils import timezone
        days = (timezone.now() - obj.created_at).days
        if days == 0:
            return 'Today'
        elif days == 1:
            return 'Yesterday'
        else:
            return f'{days} days ago'
    days_ago.short_description = 'Created'
    
    def exchange_details(self, obj):
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Requester:</strong> {}<br>'
            '<strong>Provider:</strong> {}<br>'
            '<strong>Offering:</strong> {}<br>'
            '<strong>Requesting:</strong> {}<br>'
            '<strong>Status:</strong> {}<br>'
            '<strong>Message:</strong> {}'
            '</div>',
            obj.requester.user.username, obj.provider.user.username,
            obj.skill_offered.name, obj.skill_requested.name,
            obj.get_status_display(),
            obj.message if obj.message else '<em>No message</em>'
        )
    exchange_details.short_description = 'Exchange Details'
    
    def messages_count(self, obj):
        count = obj.messages.count()
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Messages in this exchange:</strong> {}'
            '</div>',
            count
        )
    messages_count.short_description = 'Messages'

# ============================================================================
# MESSAGE ADMIN
# ============================================================================

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_display', 'receiver_display', 'content_display', 'read_status', 'created_at', 'days_ago')
    list_filter = ('is_read', 'created_at')
    search_fields = ('sender__user__username', 'receiver__user__username', 'content')
    readonly_fields = ('created_at', 'message_details')
    
    fieldsets = (
        ('Message', {
            'fields': ('sender', 'receiver', 'content', 'exchange')
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Details', {
            'fields': ('message_details',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def sender_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.sender.id, obj.sender.user.username)
    sender_display.short_description = 'From'
    
    def receiver_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.receiver.id, obj.receiver.user.username)
    receiver_display.short_description = 'To'
    
    def content_display(self, obj):
        preview = obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
        return preview
    content_display.short_description = 'Message'
    
    def read_status(self, obj):
        if obj.is_read:
            return format_html('<span style="color: green; font-weight: bold;">✓ Read</span>')
        else:
            return format_html('<span style="color: red; font-weight: bold;">✗ Unread</span>')
    read_status.short_description = 'Status'
    
    def days_ago(self, obj):
        from datetime import timedelta
        from django.utils import timezone
        days = (timezone.now() - obj.created_at).days
        if days == 0:
            return 'Today'
        elif days == 1:
            return 'Yesterday'
        else:
            return f'{days} days ago'
    days_ago.short_description = 'Sent'
    
    def message_details(self, obj):
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>From:</strong> {}<br>'
            '<strong>To:</strong> {}<br>'
            '<strong>Message:</strong><br><div style="background-color: white; padding: 8px; margin-top: 5px; border-left: 4px solid #667eea;">{}</div><br>'
            '<strong>Exchange:</strong> {}<br>'
            '<strong>Status:</strong> {}'
            '</div>',
            obj.sender.user.username, obj.receiver.user.username,
            obj.content.replace('\n', '<br>'),
            f"Exchange #{obj.exchange.id}" if obj.exchange else "No exchange",
            "Read" if obj.is_read else "Unread"
        )
    message_details.short_description = 'Message Details'

# ============================================================================
# REVIEW ADMIN
# ============================================================================

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_display', 'reviewee_display', 'rating_display', 'exchange_display', 'created_at', 'days_ago')
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer__user__username', 'reviewee__user__username', 'comment')
    readonly_fields = ('created_at', 'review_details')
    
    fieldsets = (
        ('Review', {
            'fields': ('reviewer', 'reviewee', 'rating', 'comment', 'exchange')
        }),
        ('Details', {
            'fields': ('review_details',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    def reviewer_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.reviewer.id, obj.reviewer.user.username)
    reviewer_display.short_description = 'By'
    
    def reviewee_display(self, obj):
        return format_html('<a href="/admin/skillswap/userprofile/{}/change/">{}</a>', 
                          obj.reviewee.id, obj.reviewee.user.username)
    reviewee_display.short_description = 'For'
    
    def rating_display(self, obj):
        colors = {5: 'green', 4: 'lightgreen', 3: 'orange', 2: 'coral', 1: 'red'}
        color = colors.get(obj.rating, 'gray')
        stars = '⭐' * obj.rating
        return format_html(
            '<span style="color: {}; font-weight: bold; font-size: 14px;">{} ({})</span>',
            color, stars, obj.rating
        )
    rating_display.short_description = 'Rating'
    
    def exchange_display(self, obj):
        return format_html('<a href="/admin/skillswap/skillexchange/{}/change/">Exchange #{}</a>', 
                          obj.exchange.id, obj.exchange.id)
    exchange_display.short_description = 'Exchange'
    
    def days_ago(self, obj):
        from datetime import timedelta
        from django.utils import timezone
        days = (timezone.now() - obj.created_at).days
        if days == 0:
            return 'Today'
        elif days == 1:
            return 'Yesterday'
        else:
            return f'{days} days ago'
    days_ago.short_description = 'Created'
    
    def review_details(self, obj):
        return format_html(
            '<div style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">'
            '<strong>Reviewer:</strong> {}<br>'
            '<strong>Reviewee:</strong> {}<br>'
            '<strong>Rating:</strong> {} / 5<br>'
            '<strong>Comment:</strong><br><div style="background-color: white; padding: 8px; margin-top: 5px; border-left: 4px solid #667eea;">{}</div><br>'
            '<strong>For Exchange:</strong> <a href="/admin/skillswap/skillexchange/{}/change/">#{}</a>'
            '</div>',
            obj.reviewer.user.username, obj.reviewee.user.username,
            obj.rating, obj.comment.replace('\n', '<br>'),
            obj.exchange.id, obj.exchange.id
        )
    review_details.short_description = 'Review Details'

