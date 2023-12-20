from django.shortcuts import render, redirect
from .models import Adotante
from django.contrib.auth import authenticate, login, logout

def cadastroAdotante(request):
    return render(request, 'cadastro_adotante.html')

def cadastrarAdotante(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        email = request.POST['email']
        senha = request.POST['senha']

        user = Adotante(nome=nome, idade=idade, email=email, password=senha)
        user.save()
    return render(request, '')

def loginAdotante(request):
    return render(request, 'login_adotante.html')
    
def autenticarLoginAdotante(request):
    user = authenticate(email=request.POST['email'], password=request.POST['senha'])
    if user is not None:
        login(request, user)
        return redirect('')
    return render(request, '')

def logoutAdotante(request):
    logout(request)
    return redirect('')
