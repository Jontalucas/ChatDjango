from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Doador(AbstractBaseUser):
    id_doador = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    telefone = models.CharField(max_length=16)
    cpf_cnpj = models.CharField(max_length=18)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        db_table = 'Doador'
