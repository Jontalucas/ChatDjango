from django.db import models

class User(models.Model):
    id_adotante = models.AutoField(primary_key=True)
    idade = models.DecimalField(max_digits=4, decimal_places=0)
    nome = models.TextField(max_length=100)
    email = models.EmailField(max_length=60)
    senha = models.CharField(max_length=50)
    class Meta:
        db_table = 'Adotante'