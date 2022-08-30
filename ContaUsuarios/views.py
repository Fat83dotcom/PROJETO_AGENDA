from django.contrib import messages
from django.shortcuts import render
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login(request):
    return render(request, 'ContaUsuario/login.html')


def logout(request):
    return render(request, 'ContaUsuario/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'ContaUsuario/cadastro.html')

    nome = request.POST.get('Nome')
    sobreNome = request.POST.get('sobreNome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')

    try:
        validate_email(email)
    except Exception:
        messages.error(request, 'Informe um endereço de email válido.')
        return render(request, 'ContaUsuario/cadastro.html')

    if not nome or not sobreNome or not usuario or not email \
            or not senha1 or not senha2:
        messages.add_message(request, messages.ERROR, 'Preencha todos os campos !')
        return render(request, 'ContaUsuario/cadastro.html')
    else:

        if len(usuario) < 6:
            messages.error(request, 'O usuário deve conter no mínimo 6 caracteres.')

        if len(senha1) < 6 or len(senha2) < 6:
            messages.error(request, 'A senha deve conter no mínimo 6 caracteres.')

        if senha1 != senha2:
            messages.error(request, 'As senhas não conferem.')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe.')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já existe.')

        return render(request, 'ContaUsuario/cadastro.html')

    # return render(request, 'ContaUsuario/cadastro.html')


def dashboard(request):
    return render(request, 'ContaUsuario/dashboard.html')
