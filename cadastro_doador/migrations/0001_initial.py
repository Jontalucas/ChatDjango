# Generated by Django 4.1.1 on 2023-12-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_doador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=16)),
                ('cpf_cnpj', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=60)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]