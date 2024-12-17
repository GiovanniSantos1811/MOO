from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("convites/<str:apelido>/", views.convites, name="convites"),
    path("convites/<str:apelido>/criacao", views.criacao, name="criacao"),
    path("convites/<str:apelido>/visualizar", views.visualizar, name="visualizar")
]