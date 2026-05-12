from django import forms
from .models import Appcontent

class JobForm(forms.ModelForm):
    class Meta: 
        model = Appcontent
        fields = ['title', 'salary', 'location','date', 'company']
        labels = {
            'title': 'Job Title',
            'company': 'Company Name',
            'salary': 'Salary (£)',
            'location': 'Location',
            'date': 'Date Applied',
            'status': 'Application Status',
        }

        widgets = { #Placeholders
            'company': forms.TextInput(attrs={'placeholder': '~ Google'}),
            'title': forms.TextInput(attrs={'placeholder': '~ Software Engineer'}),
            'date': forms.DateInput(attrs={'type': 'date'})
        }