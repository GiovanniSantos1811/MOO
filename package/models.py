# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppPerfilJogador(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=50)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(unique=True, max_length=50)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30)
    teste = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'app_perfil_jogador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Convite(models.Model):
    jogador1 = models.OneToOneField('PerfilJogador', models.DO_NOTHING, db_column='jogador1', primary_key=True)  # The composite primary key (jogador1, jogador2, jogo, data_convite) found, that is not supported. The first column is selected.
    jogador2 = models.ForeignKey('PerfilJogador', models.DO_NOTHING, db_column='jogador2', related_name='convite_jogador2_set')
    jogo = models.ForeignKey('Jogo', models.DO_NOTHING, db_column='jogo')
    data_convite = models.DateField()
    mensagem = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convite'
        unique_together = (('jogador1', 'jogador2', 'jogo', 'data_convite'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    jogador = models.ForeignKey('PerfilJogador', models.DO_NOTHING, db_column='jogador')

    class Meta:
        managed = False
        db_table = 'jogos_jogador'
        unique_together = (('jogo', 'jogador'),)


class PerfilJogador(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    apelido = models.CharField(unique=True, max_length=50)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_jogador'
