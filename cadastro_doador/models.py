from django.db import models

class User(models.Model):
    id_doador = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=100)
    telefone = models.CharField(max_length=16)
    cpf_cnpj = models.CharField(max_length=18)
    email = models.EmailField(max_length=60)
    senha = models.CharField(max_length=50)
    class Meta:
        db_table = 'Doador'