from django import forms
from .models import Appcontent

class JobForm(forms.ModelForm):
    class Meta: 
        model = Appcontent
        fields = ['title', 'salary', 'location', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }