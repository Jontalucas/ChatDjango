from django.shortcuts import render, redirect
from .models import Doador
from django.contrib.auth import authenticate, login, logout

def cadastroDoador(request):
    return render(request, 'cadastro_doador.html')

def cadastrarDoador(request):
    user = Doador.objects.create_user(
        nome = request.POST['nome'],
        telefone = request.POST['telefone'],
        cpf_cnpj = request.POST['cpf_cnpj'],
        email = request.POST['email'],
        password = request.POST['senha']
    )
    user.save()
    return render(request, '')

def loginDoador(request):
    return render(request, 'login_doador.html')
    
def autenticarLoginDoador(request):
    user = authenticate(email=request.POST['email'], password=request.POST['senha'])
    if user is not None:
        login(request, user)
        return redirect('')
    return render(request, '')

def logoutDoador(request):
    logout(request)
    return redirect('')