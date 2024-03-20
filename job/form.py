# forms.py
from django import forms

from .models import Job

class CreateJobForm(forms.ModelForm):
   
    class Meta:
        model = Job
        exclude = ('user', 'company')  # Exclude the 'user' and 'company' fields from the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'ideal_candidate': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }




class UpdateJobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ('user', 'company')  # Exclude the 'user' field from the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'requirements': forms.TextInput(attrs={'class': 'form-control'}),
        }
