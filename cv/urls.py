from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_home, name='cv_home'),
    path('qualification/new/', views.qualification_edit, name='qualification_edit'),
]