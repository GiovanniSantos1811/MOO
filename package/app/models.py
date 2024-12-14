from django.db import models

class Perfil_Jogador(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
