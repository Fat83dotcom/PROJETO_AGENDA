from django.shortcuts import render, redirect  # get_object_or_404
from .models import Contato
# from django.http import Http404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='login')
def index(request):

    contatos = Contato.objects.order_by('-id')
    paginador = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginador.get_page(page)
    return render(request, 'contato/index.html', {
        'contatos': contatos
    })


@login_required(redirect_field_name='login')
def contatos(request, contato_id):
    # contato = get_object_or_404(Contato, id=contato_id)  # maneira mais simples do que com o try
    try:
        contato = Contato.objects.get(id=contato_id)
        if not contato.mostrar:
            # raise Http404
            messages.add_message(request,
                                 messages.ERROR,
                                 'O contato não pode ser exibido!')
            return redirect('index')

        return render(request, 'contato/viewer_contato.html', {
            'contato': contato
        })
    except (Contato.DoesNotExist,):
        # raise Http404
        messages.add_message(request,
                             messages.ERROR,
                             'A página não Existe !')
        return redirect('index')
