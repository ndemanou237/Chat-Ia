from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model

class CustomSignupForm(UserCreationForm):
    username = forms.CharField(label='Nom d\'utilisateur',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}
                               ))
    email = forms.CharField(label='Adresse email',
                                   widget=forms.EmailInput(
                                       attrs={'class': 'form-control'}
                                   ))
    password1 = forms.CharField(label='Mot de passe',
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-control'}
                                   ))
    password2 = forms.CharField(label='Confirmer le mot de passe',
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-control'}
                                   ))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
