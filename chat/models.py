from django.db import models
from adotante.models import Adotante
from doador.models import Doador

class Chat(models.Model):
    id_chat = models.AutoField(primary_key=True)
    doador = models.ForeignKey(Doador, on_delete = models.CASCADE)
    adotante = models.ForeignKey(Adotante, on_delete = models.CASCADE)
    data_atualizacao = models.DateField(auto_now_add = True)
    data_criacao = models.DateField(auto_now_add = True)
    class Meta:
        db_table = 'Chat'
