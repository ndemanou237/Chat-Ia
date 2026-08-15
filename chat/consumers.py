import json
import ollama
import markdown2
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Project, ChatMessage
from asgiref.sync import sync_to_async

User = get_user_model()

class ChatConsummer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.room_group_name = f"chat_{self.project_id}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data = json.loads(text_data)
        user_message = data.get('message')

        await self.send(text_data=json.dumps({
            'message': user_message, "sender": "user"
        }))
        project = await self.get_project()
        if not project:
            return None

        
        raw_markdown_response = ""
        stream = ollama.chat(
            model='deepseek-r1:1.5b',
            messages=[{'role': "user", "content": user_message}],
            stream=True
        )

        for chunck in stream:
            raw_markdown_response += chunck['message']['content']
            formatted_html = markdown2.markdown(raw_markdown_response)
            await self.send(text_data=json.dumps({
                'message': formatted_html, "sender": "ai"
            }))
            await asyncio.sleep(0.05)

        await self.save_message(project, self.scope['user'], user_message, formatted_html)
        await self.send(text_data=json.dumps({
            'close': True
        }))    
        await self.close()

    @sync_to_async
    def get_project(self):
        try:
            project = Project.objects.get(id=self.project_id)
            return project
        except Project.DoesNotExist:
            return None

    @sync_to_async
    def save_message(self, project, user, user_message, ai_response):
        ChatMessage.objects.create(
            project= project, user=user, message=user_message, response=ai_response
        )        
