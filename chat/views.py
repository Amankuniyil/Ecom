from django.shortcuts import render,get_object_or_404,redirect
from user.models import Account
from .models import Message,ChatGroup
from .forms import ChatBox
# Create your views here.


def users(request):
    users=Account.objects.all()
    return render(request,'users.html',{'users':users})

def message(request,chatroom_name):
    form=ChatBox(request.POST)

  
    
    chat, created=ChatGroup.objects.get_or_create(group_name=chatroom_name)
      

    group=chat
    message=Message.objects.filter(group=group)
   

    if request.method=='POST':
        i=request.user
        u=Account.objects.get(id=4)

        user = u
        form=ChatBox(request.POST)
       

        a, created=ChatGroup.objects.get_or_create(group_name=chatroom_name)
      

        group=a
        author=user
        if form.is_valid():
            body = form.cleaned_data.get('Body') 

        else:
            form = ChatBox()
    


            return render(request, 'message.html', {'messages':message,'form': form})

        Message.objects.create(group=chatroom_name,author=author,Body=body)

    
        
        message=Message.objects.filter(group=chatroom_name)
       
       

        return redirect('message')
    else:
        form = ChatBox()
    


    return render(request, 'message.html', {'messages':message,'form': form})


# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Signal logic here
        print(f"New user created: {instance.username}")
        # You can also send an email, or call an external API, etc.
