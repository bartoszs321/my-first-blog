from django.urls import path
from . import views

urlpatterns = [
    path('cv/', views.cv_home, name='cv_home'),
]