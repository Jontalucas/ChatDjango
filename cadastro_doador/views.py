from django.shortcuts import render
from django.http import HttpResponse
from .models import User



def cadastro_doador(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        cpf_cnpj = request.POST['cpf_cnpj']
        email = request.POST['email']
        senha = request.POST['senha']
        
        user = User(nome=nome, telefone=telefone, cpf_cnpj=cpf_cnpj, email=email, senha=senha)
        user.save()

        return HttpResponse('Cadastro realizado com sucesso!')

    return render(request, 'cadastro_doador.html')
def login_doador(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try: 
            user = User.objects.get(email=email, senha=senha)
            if user is not None:
                logado = True
                return HttpResponse('Login realizado com sucesso!')
        except:
            return HttpResponse('Usuário ou senha inválidos.')

    return render(request, 'login_doador.html')

def procurar_doador(request):
    
    try:
        user = User.objects.get(nome=request)
        return user
    except:
            return HttpResponse('Doador não existe')
    
    