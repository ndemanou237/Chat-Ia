from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "chat/project_list.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by('created_at')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'chat/project_form.html'
    success_url = reverse_lazy('chat:project_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Projet crée avec succès')
        return super().form_valid(form)  

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'chat/project_form.html'  
    success_url = reverse_lazy('chat:project_list')

    def form_valid(self, form):
        messages.success(self.request, 'Projet mis à jour avex succes')
        return super().form_valid(form)

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)  

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'chat/project_confirm_delete.html'
    success_url = reverse_lazy('chat:project_list')

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Projet supprimé avec succès')
        return super().delete(request, *args, **kwargs)   

class ChatView(LoginRequiredMixin, View):
    template_name = 'chat/chat.html'
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['project_id'], owner=request.user)
        messages = project.chatmessage_set.all()
        projects = Project.objects.filter(owner=request.user)
        context = {
            'project': project,
            'messages_chat': messages,
            'projects': projects
        }                       
        return render(request, self.template_name, context)
