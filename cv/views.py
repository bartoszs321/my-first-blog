from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cv_home(request):
    return render(request, 'cv/cv_home.html')