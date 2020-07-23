from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Qualification, Experience, Interest
from .forms import QualificationForm, ExperienceForm, InterestForm

def cv_home(request):
    qualifications = Qualification.objects.all()
    experiences = Experience.objects.all()
    interests = Interest.objects.all()
    return render(request, 'cv/cv_home.html', {
        'qualifications' : qualifications,
        'experiences' : experiences,
        'interests' : interests,
     })

def qualification_edit(request):
    if request.method == "POST":
        form = QualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.save()
            return redirect('cv_home')
    else:
        form = QualificationForm()
    return render(request, 'cv/qualification_edit.html', {'form': form})

def experience_edit(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_home')
    else:
        form = ExperienceForm()
    return render(request, 'cv/experience_edit.html', {'form': form})

def interest_edit(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.save()
            return redirect('cv_home')
    else:
        form = InterestForm()
    return render(request, 'cv/interest_edit.html', {'form': form})