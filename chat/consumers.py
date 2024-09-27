# consumers.py

import json
from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import get_object_or_404
from .models import *
from asgiref.sync import async_to_sync
from django.template.loader import render_to_string
from django.shortcuts import render,get_object_or_404,redirect

import json
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.shortcuts import get_object_or_404
from .models import ChatGroup, Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
        chat, created=ChatGroup.objects.get_or_create(group_name=self.chatroom_name)
        

        # Join the chatroom group
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave the chatroom group
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['Body']

        # Create a new message
        message = Message.objects.create(
            Body=body,
            author=self.user,
            group=self.chatroom,
        )
        print(self.chatroom_name)

        message_data = {
            'author': self.user.first_name,
            'message': body,
            'created': message.created.strftime('%Y-%m-%d %H:%M:%S'),
            'user':self.user.id
        }

        # Send the message data to the chatroom group
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name,
            {
                'type': 'chat_message',
                'message': message_data
            }
        )

    def chat_message(self, event):
        # Extract the message data from the event
        message_data = event['message']

        # Send the message data to the WebSocket
        self.send(text_data=json.dumps(message_data))
