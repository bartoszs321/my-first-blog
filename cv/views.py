from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cv_home(request):
    return HttpResponse('<html><title>Bartosz\'s CV</title></html>')