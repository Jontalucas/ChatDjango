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

def login_adotante(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try: 
            user = User.objects.get(email=email, senha=senha)
            if user is not None:
                logado_adotante = True
                return HttpResponse('Login realizado com sucesso!')
        except:
            return HttpResponse('Usuário ou senha inválidos.')

    return render(request, 'login_adotante.html')

def procurar_adotante(request):
    
    try:
        user = User.objects.get(nome=request)
        return user
    except:
            return HttpResponse('Adotante não existe')