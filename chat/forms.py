from django import forms
from .models import Message

class ChatBox(forms.ModelForm):

    class Meta:
        model=Message

        fields=['Body']