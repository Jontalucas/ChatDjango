from django.db import models
from doador.models import Doador

class Localizacao(models.Model):
    id_localizacao = models.AutoField(primary_key=True)
    doador = models.ForeignKey(Doador, on_delete = models.CASCADE)
    cep = models.DecimalField(max_digits=10, decimal_places=0)
    class Meta:
        db_table = 'Localizacao'
