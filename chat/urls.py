from django.urls import path
from .views import users,message


# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('message/<str:chatroom_name>', message, name='message'),
]
