from django.urls import path
from .views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

app_name = 'chat'
urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    
]
