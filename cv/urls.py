from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_home, name='cv_home'),
    path('qualification/new/', views.qualification_new, name='qualification_new'),
    path('experience/new/', views.experience_new, name='experience_new'),
    path('interest/new/', views.interest_new, name='interest_new'),
    path('profile/new/', views.profile_new, name='profile_new'),
    path('profile/<pk>/remove/', views.profile_remove, name='profile_remove'),
    path('qualification/<pk>/remove/', views.qualification_remove, name='qualification_remove'),
    path('experience/<pk>/remove/', views.experience_remove, name='experience_remove'),
    path('interest/<pk>/remove/', views.interest_remove, name='interest_remove'),
    path('profile/<pk>/edit/', views.profile_edit, name='profile_edit'),
    path('qualification/<pk>/edit/', views.qualification_edit, name='qualification_edit'),
    path('experience_edit/<pk>/edit/', views.experience_edit, name='experience_edit'),
    path('interest/<pk>/edit/', views.interest_edit, name='interest_edit'),
]