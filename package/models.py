# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Convite(models.Model):
    jogador1 = models.OneToOneField('PerfilJogador', models.DO_NOTHING, db_column='jogador1', primary_key=True)  # The composite primary key (jogador1, jogador2, jogo, data_convite) found, that is not supported. The first column is selected.
    jogador2 = models.ForeignKey('PerfilJogador', models.DO_NOTHING, db_column='jogador2', to_field='email', related_name='convite_jogador2_set')
    jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='jogo')
    data_convite = models.DateField()
    mensagem = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convite'
        unique_together = (('jogador1', 'jogador2', 'jogo', 'data_convite'),)


class Jogo(models.Model):
    titulo = models.CharField(primary_key=True, max_length=50)
    genero = models.CharField(max_length=30, blank=True, null=True)
    desenvolvedor = models.CharField(max_length=100, blank=True, null=True)
    publicadora = models.CharField(max_length=50, blank=True, null=True)
    data_lancamento = models.DateField()
    classificacao_etaria = models.DecimalField(max_digits=65535, decimal_places=65535)

    class Meta:
        managed = False
        db_table = 'jogo'


class JogosJogador(models.Model):
    jogo = models.OneToOneField(Jogo, models.DO_NOTHING, db_column='jogo', primary_key=True)  # The composite primary key (jogo, jogador) found, that is not supported. The first column is selected.
    jogador = models.ForeignKey('PerfilJogador', models.DO_NOTHING, db_column='jogador', to_field='email')

    class Meta:
        managed = False
        db_table = 'jogos_jogador'
        unique_together = (('jogo', 'jogador'),)


class PerfilJogador(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    apelido = models.CharField(unique=True, max_length=50)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_jogador'
