from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil_Jogador

# Create your views here.
def home(request):
    return render(request, "home.html")

def cadastro(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        email = request.POST['email']
        nome = request.POST['nome']
        apelido = request.POST['apelido']
        data_nascimento = request.POST['dataNascimento']
        senha = request.POST['senha']

        #print("Email: ", email, " / senha: ", senha) #Debug

        # Criar um novo usuário no banco de dados
        jogador = Perfil_Jogador.objects.create(
            email=email,
            nome=nome,
            apelido=apelido,
            data_nascimento=data_nascimento,
            senha=senha
        )

        # Redirecionar para a página de login após o cadastro
        return redirect('login')
    else:
        return render(request, 'cadastro.html')

def login(request):
    return render(request, "login.html")
