from django.urls import path
from .views import *


urlpatterns = [
    path('home', home, name='home'),
    path('usuarios', cadastrar_usuario, name='cadastrar_usuario'),
    path('projeto', cadastrar_projeto, name='cadastrar_projeto'),
    path('', logar_usuario, name='login'),
    path('logout', deslogar_usuario, name='logout'),
]
