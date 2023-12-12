from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

def chat(request):
    global messages
    messages = Message.objects.all().only('corpo')
    
    if request.method == 'POST':
        message = request.POST['message']

        message = Message(corpo=message)
        message.save()

    return render(request, 'chat.html', {'messages': messages})