# Generated by Django 4.2.17 on 2024-12-13 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_perfil_jogador_teste_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_jogador',
            name='teste',
        ),
    ]
