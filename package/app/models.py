from django.db import models

class Perfil_Jogador(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    classificacao_etaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Convite(models.Model):
    jogador1 = models.ForeignKey(Perfil_Jogador, on_delete=models.CASCADE, related_name='convites_jogador1')
    jogador2 = models.ForeignKey(Perfil_Jogador, on_delete=models.CASCADE, related_name='convites_jogador2')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_convite = models.DateField()
    mensagem = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
