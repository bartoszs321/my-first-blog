from django.shortcuts import render
from django.http import HttpResponse
from .models import Qualification

def cv_home(request):
    qualifications = Qualification.objects.all()
    return render(request, 'cv/cv_home.html', {'qualifications' : qualifications})