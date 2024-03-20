from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude = ('user',)  # Exclude the 'user' field from the form

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'upload_resume': forms.FileInput(attrs={'class': 'form-control'}),

        }
