from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email')
    list_display_links = ('telefone', 'nome')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
