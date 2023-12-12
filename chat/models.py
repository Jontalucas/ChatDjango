from django.db import models

class Message(models.Model):
    id_mensagem = models.AutoField(primary_key=True)
    corpo = models.TextField()
    enviada = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Mensagem'
        ordering = ('-enviada',)