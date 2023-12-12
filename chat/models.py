from django.db import models
from cadastro_adotante.models import User as Adotante
from cadastro_doador.models import User as Doador

class Message(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    corpo = models.TextField()
    enviada = models.DateTimeField(auto_now_add=True)
    id_chat = models.ForeignKey('Chat', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Mensagem'
        ordering = ('-enviada',)
        
class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)
    adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Chat'