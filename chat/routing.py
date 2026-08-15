from django.urls import re_path
from .consumers import ChatConsummer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<project_id>\w+)", ChatConsummer.as_asgi()),
    
]