from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil_Jogador
from django.contrib import messages

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
        return redirect('convites', apelido=apelido)
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        print("email: ", email)
        
        try:
            # Buscar o usuário na tabela
            perfil = Perfil_Jogador.objects.get(email=email)
            
            # Verificar se a senha é válida
            if (senha == perfil.senha):
                # Armazenar o login na sessão
                request.session['user_id'] = perfil.id
                request.session['user_apelido'] = perfil.apelido
                return redirect("convites", apelido=perfil.apelido)  # Redirecionar após login bem-sucedido
            else:
                messages.error(request, "Senha incorreta.")
        except Perfil_Jogador.DoesNotExist:
            messages.error(request, "Email não encontrado.")
    
    return render(request, "login.html")

def convites(request, apelido):
    return render(request, "convites.html", {"apelido": apelido})
