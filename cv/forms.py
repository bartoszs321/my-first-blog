from django import forms

from .models import Qualification, Experience, Interest, Profile

class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('title', 'date_started', 'date_completed', 'awarding_body', 'text',)

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('title', 'company', 'date_started', 'date_completed', 'text',)

class InterestForm(forms.ModelForm):

    class Meta:
        model = Interest
        fields = ('title', 'text',)

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('text',)