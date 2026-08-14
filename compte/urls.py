from django.urls import path
from .views import *

app_name = 'compte'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    
]
