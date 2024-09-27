from django.urls import path,re_path
from .consumers import *

websocket_urlpatterns = [
    path('ws/chatroom/<str:chatroom_name>/', ChatConsumer.as_asgi()),
]