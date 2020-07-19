from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Qualification
from .forms import QualificationForm

def cv_home(request):
    qualifications = Qualification.objects.all()
    return render(request, 'cv/cv_home.html', {'qualifications' : qualifications})

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