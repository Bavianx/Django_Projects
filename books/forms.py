from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book        #Identifies the DB to save the form data to ("when this form is submitted, save it to the Book table")
        fields = ['isbn', 'title', 'author', 'available'] #Identifies the specific fields are shown within the form. ("only show these fields to the user, not all of them")