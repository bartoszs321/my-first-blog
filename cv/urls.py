from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_home, name='cv_home'),
    path('qualification/new/', views.qualification_edit, name='qualification_edit'),
    path('experience/new/', views.experience_edit, name='experience_edit'),
    path('interest/new/', views.interest_edit, name='interest_edit'),
    path('profile/new/', views.profile_edit, name='profile_edit'),
    path('profile/<pk>/remove/', views.profile_remove, name='profile_remove'),
    path('qualification/<pk>/remove/', views.qualification_remove, name='qualification_remove'),
    path('experience/<pk>/remove/', views.experience_remove, name='experience_remove'),
    path('interest/<pk>/remove/', views.interest_remove, name='interest_remove'),
]