from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from .models import Chat
from cadastro_doador.views import procurar_doador
from cadastro_adotante.views import procurar_adotante

def chat(request):
    global messages
    messages = Message.objects.all().only('corpo')
    
    if request.method == 'POST':
        message = request.POST['message']

        message = Message(corpo=message)
        message.save()

    return render(request, 'chat.html', {'messages': messages})

def criar_chat(request):
    if request.method == 'POST':
        doador = request.POST['doador']
        adotante = request.POST['adotante']

        user_doador = procurar_doador(doador)
        user_adot = procurar_adotante(adotante)
        
        chat = Chat(doador=user_doador, adotante=user_adot)
        chat.save()
        
    return render(request, 'criar_chat.html')

    