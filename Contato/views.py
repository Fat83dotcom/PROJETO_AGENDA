from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contato/index.html', {
        'contatos': contatos
    })


def contatos(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contato/viewer_contato.html', {
        'contato': contato
    })
