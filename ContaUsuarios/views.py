from django.shortcuts import render


def login(request):
    return render(request, 'ContaUsuario/login.html')


def logout(request):
    return render(request, 'ContaUsuario/logout.html')


def cadastro(request):
    
    return render(request, 'ContaUsuario/cadastro.html')


def dashboard(request):
    return render(request, 'ContaUsuario/dashboard.html')
