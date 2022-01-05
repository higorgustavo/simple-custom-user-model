from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.models import Projeto
from .forms import ProjetoForm, UserCreationForm

@login_required
def home(request):
    projetos = Projeto.objects.filter(empresa=request.user.empresa).all()
    context = {
        "projetos": projetos
    }
    return render(request, "home.html", context)


@login_required
def cadastrar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.empresa = request.user.empresa
            projeto.save()
            return redirect('home')
    else:
        form = ProjetoForm()

    context = {
        "form": form
    }
    return render(request, "cadastrar_projeto.html", context)


def cadastrar_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context = {
        "form": form
    }
    return render(request, "cadastrar_usuario.html", context)


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()

    context = {
        "form_login": form_login
    }
    return render(request, "login.html", context)


def deslogar_usuario(request):
    logout(request)
    return redirect('login')
