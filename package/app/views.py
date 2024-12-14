from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Perfil_Jogador, Jogo, Convite
from django.contrib import messages
from datetime import date

#Auxiliar functions
def age(data):
    # Obter a data atual
    data_atual = date.today()
    
    # Calcular a diferença em anos
    idade = data_atual.year - data.year
    
    # Ajustar caso o aniversário ainda não tenha ocorrido no ano atual
    if (data_atual.month, data_atual.day) < (data.month, data.day):
        idade -= 1  # Não fez aniversário ainda este ano
    
    return idade


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

def criacao(request, apelido):
    #Passando os jogos armazenados no banco de dados para o select da página
    jogos = Jogo.objects.all() #Selecionando todos os jogos disponíveis

    if request.method == "POST":
        jogador2 = request.POST.get('apelido')
        jogo_id = request.POST.get('titulo_jogo')
        data_convite = request.POST.get('data_convite')
        mensagem = request.POST.get('mensagem')

        #Checagem da existência do jogador2
        try:
            perfil = Perfil_Jogador.objects.get(apelido=jogador2)
            jogo = Jogo.objects.get(id=jogo_id)
            
            #Garantindo que o usuário não esteja tentando mandar convite para si mesmo
            if (jogador2 != apelido):
                #Garantindo que ambos os jogadores tenham idade suficiente para a classificação indicativa do jogo selecionado
                idade1 = age(Perfil_Jogador.objects.get(apelido=apelido).data_nascimento)
                idade2 = age(perfil.data_nascimento)
                if (idade1 >= jogo.classificacao_etaria and idade2 >= jogo.classificacao_etaria):
                    #Criando um convite novo na tabela de Convites
                    convite = Convite.objects.create(
                        jogador1 = Perfil_Jogador.objects.get(apelido=apelido), #Jogador que está enviando o convite
                        jogador2 = perfil, #Jogador que está recebendo o convite
                        jogo = jogo,
                        data_convite = data_convite,
                        mensagem = mensagem
                    )

                    return redirect('convites', apelido=apelido)

                else:
                    messages.error(request, "O jogo escolhido é inapropriado para a idade de um ou mais jogadores")
            else:
                messages.error(request, "O convite precisa ser feito para um outro jogador!")
        except Perfil_Jogador.DoesNotExist:
            messages.error(request, 'Jogador não encontrado')
    
    return render(request, "criacao.html", {"apelido": apelido, "jogos":jogos}) #Renderizando a página com as informações dos jogos cadastrados
