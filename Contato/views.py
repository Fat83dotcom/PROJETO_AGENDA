from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.http import Http404


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contato/index.html', {
        'contatos': contatos
    })


def contatos(request, contato_id):
    # contato = get_object_or_404(Contato, id=contato_id)  # maneira mais simples do que com o try
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contato/viewer_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExist:
        raise Http404
