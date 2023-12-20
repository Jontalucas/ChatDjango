# Generated by Django 4.1.1 on 2023-12-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adotante',
            fields=[
                ('id_doador', models.AutoField(primary_key=True, serialize=False)),
                ('idade', models.DecimalField(decimal_places=0, max_digits=4)),
                ('nome', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=60)),
                ('senha', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Adotante',
            },
        ),
    ]