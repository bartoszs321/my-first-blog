from django.contrib import admin
from .models import Qualification, Experience, Interest, Profile

# Register your models here.
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Interest)
admin.site.register(Profile)