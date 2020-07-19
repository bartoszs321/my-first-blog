from django import forms

from .models import Qualification

class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ('title', 'date_started', 'date_completed', 'awarding_body', 'text',)