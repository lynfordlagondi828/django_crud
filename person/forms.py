from django import forms
from .models import Person

class PersonForms(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['lastname', 'middlename', 'firstname', 'degree']
