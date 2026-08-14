from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TelInput(
            attrs={'class': 'form-control', 'placeholder': 'Nom du projet'}
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Description'}
        )
    )
    
    class Meta:
        model = Project
        fields = ['name', 'description']