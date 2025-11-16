from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='index'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard & Profile
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    
    # Skills
    path('skill/create/', views.skill_create, name='skill_create'),
    path('skill/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skill/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skill/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    path('browse-skills/', views.browse_skills, name='browse_skills'),
    
    # Exchanges
    path('exchange/<int:skill_id>/request/', views.skill_exchange_request, name='exchange_request'),
    path('exchange/<int:exchange_id>/respond/', views.exchange_respond, name='exchange_respond'),
    path('exchange/<int:exchange_id>/complete/', views.exchange_complete, name='exchange_complete'),
    
    # Reviews
    path('review/<int:exchange_id>/create/', views.create_review, name='create_review'),
    
    # Messaging
    path('messages/', views.messages_list, name='messages_list'),
    path('chat/<str:username>/', views.chat_view, name='chat_view'),
    path('exchange/<int:exchange_id>/chat/', views.exchange_chat_view, name='exchange_chat'),
]
