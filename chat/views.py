from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "chat/project_list.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
