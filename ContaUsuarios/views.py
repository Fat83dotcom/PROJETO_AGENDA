from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'ContaUsuario/login.html')

    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, email=email, password=senha)

    if not user:
        messages.error(request, 'Email ou Senha inválidos.')
        return render(request, 'ContaUsuario/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com Sucesso.')
        return redirect('dashboard')


def logout(request):
    return render(request, 'ContaUsuario/logout.html')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'ContaUsuario/cadastro.html')

    # recebe os dados cadastrados na pagina html

    nome = request.POST.get('Nome').title()
    sobreNome = request.POST.get('sobreNome').title()
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')

    # essa parte faz a validação da página

    try:
        validate_email(email)
    except Exception:
        messages.error(request, 'Informe um endereço de email válido.')
        return render(request, 'ContaUsuario/cadastro.html')

    if not nome or not sobreNome or not usuario or not email \
            or not senha1 or not senha2:
        messages.add_message(request, messages.ERROR, 'Preencha todos os campos !')
        return render(request, 'ContaUsuario/cadastro.html')

    try:
        if User.objects.filter(username=usuario).exists():
            raise messages.error(request, 'Usuário já existe.')

        if User.objects.filter(email=email).exists():
            raise messages.error(request, 'E-mail já existe.')

        if len(usuario) < 8:
            raise messages.error(request, 'O usuário deve conter no mínimo 8 caracteres.')

        if len(senha1) < 8 or len(senha2) < 8:
            raise messages.error(request, 'A senha deve conter no mínimo 8 caracteres.')

        if senha1 != senha2:
            raise messages.error(request, 'As senhas não conferem.')
    except Exception:
        return render(request, 'ContaUsuario/cadastro.html')

    user = User.objects.create_user(username=usuario, password=senha1,
                                    email=email, first_name=nome,
                                    last_name=sobreNome)
    user.save()
    messages.success(request, 'Usuário cadastrado com Sucesso.')
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'ContaUsuario/dashboard.html')
