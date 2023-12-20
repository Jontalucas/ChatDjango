from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class Adotante(AbstractBaseUser):  
    id_doador = models.AutoField(primary_key = True)
    idade = models.DecimalField(max_digits=4, decimal_places=0)
    nome = models.EmailField(max_length=100)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        db_table = 'Adotante'