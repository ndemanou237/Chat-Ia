from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomSignupForm, CustomLoginForm
from django.contrib.auth import login, logout

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'compte/signup.html'
    success_url = reverse_lazy('chat:project_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'compte/login.html'

def logout_view(request):
    logout(request)
    return redirect('compte:login')
