from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def cadastro_adotante(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        email = request.POST['email']
        senha = request.POST['senha']

        user = User(nome=nome, idade=idade, email=email, senha=senha)
        user.save()

        return HttpResponse('Cadastro realizado com sucesso!')

    return render(request, 'cadastro_adotante.html')