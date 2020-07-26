from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Qualification, Experience, Interest, Profile
from .forms import QualificationForm, ExperienceForm, InterestForm, ProfileForm

def cv_home(request):
    qualifications = Qualification.objects.all()
    experiences = Experience.objects.all()
    interests = Interest.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'cv/cv_home.html', {
        'qualifications' : qualifications,
        'experiences' : experiences,
        'interests' : interests,
        'profiles' : profiles,
     })

@login_required
def qualification_new(request):
    if request.method == "POST":
        form = QualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.save()
            return redirect('cv_home')
    else:
        form = QualificationForm()
    return render(request, 'cv/qualification_edit.html', {'form': form})

@login_required
def qualification_edit(request, pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    if request.method == "POST":
        form = QualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.save()
            return redirect('cv_home')
    else:
        form = QualificationForm(instance=qualification)
    return render(request, 'cv/qualification_edit.html', {'form': form})

@login_required
def experience_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_home')
    else:
        form = ExperienceForm()
    return render(request, 'cv/experience_edit.html', {'form': form})

@login_required
def experience_edit(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('cv_home')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'cv/experience_edit.html', {'form': form})

@login_required
def interest_new(request):
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.save()
            return redirect('cv_home')
    else:
        form = InterestForm()
    return render(request, 'cv/interest_edit.html', {'form': form})

@login_required
def interest_edit(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    if request.method == "POST":
        form = InterestForm(request.POST, instance=interest)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.save()
            return redirect('cv_home')
    else:
        form = InterestForm(instance=interest)
    return render(request, 'cv/interest_edit.html', {'form': form})

@login_required
def profile_new(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('cv_home')
    else:
        form = ProfileForm()
    return render(request, 'cv/profile_edit.html', {'form': form})

@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('cv_home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'cv/profile_edit.html', {'form': form})
    
@login_required
def profile_remove(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    profile.delete()
    return redirect('cv_home')

@login_required
def qualification_remove(request, pk):
    qualification = get_object_or_404(Qualification, pk=pk)
    qualification.delete()
    return redirect('cv_home')

@login_required
def experience_remove(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    experience.delete()
    return redirect('cv_home')

@login_required
def interest_remove(request, pk):
    interest = get_object_or_404(Interest, pk=pk)
    interest.delete()
    return redirect('cv_home')