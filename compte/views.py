from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomSignupForm
from django.contrib.auth import login

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'compte/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
