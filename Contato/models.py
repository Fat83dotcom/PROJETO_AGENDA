from django.utils import timezone
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    dt_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome
