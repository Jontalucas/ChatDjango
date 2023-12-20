"""adote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import chat.views
import adotante.views
import doador.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat.views.chat, name='chat'),
    path('chat/<str:room_name>/', chat.views.room, name='room'),
    path('cadastro_doador/', doador.views.cadastroDoador),
    path('cadastrar_doador/', doador.views.cadastrarDoador),
    path('cadastro_adotante/', adotante.views.cadastroAdotante),
    path('cadastrar_adotante/', adotante.views.cadastrarAdotante),
    path('login_adotante/', adotante.views.loginAdotante),
    path('login_doador/', doador.views.loginDoador),
    path('autenticar_login_adotante', adotante.views.autenticarLoginAdotante),
    path('autenticar_login_doador', doador.views.autenticarLoginDoador),
    path('logout_doador/', doador.views.logoutDoador),
    path('logout_adotante/', adotante.views.logoutAdotante)
]
