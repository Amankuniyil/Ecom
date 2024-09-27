from django.db import models
from user.models import *

# Create your models here.


class ChatGroup(models.Model):
    group_name=models.CharField(max_length=150,unique=True)


class Message(models.Model):
    group=models.ForeignKey(ChatGroup,on_delete=models.CASCADE)
    author=models.ForeignKey(Account,on_delete=models.CASCADE)
    Body=models.TextField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)

