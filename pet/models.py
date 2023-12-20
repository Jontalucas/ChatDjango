from django.db import models
from doador.models import Doador

class Pet(models.Model):
    id_pet = models.AutoField(primary_key = True)
    doador = models.ForeignKey(Doador, on_delete = models.CASCADE)
    idade = models.DecimalField(max_digits=4, decimal_places=0)
    saude = models.TextField(max_length=1000)
    historia = models.TextField(max_length=1500)
    especie = models.TextField(max_length=50)
    foto = models.TextField(max_length=200)
    class Meta:
        db_table = 'Pet'
    