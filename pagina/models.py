from django.db import models
from core.opcoes import CATEGORIA, TIPO
# Create your models here.

class Documenmto(models.Model):
    titulo = models.CharField(max_length=520, blank=True, null=True,default="")
    instituicao = models.CharField(max_length=220, blank=True, null=True,default="")
    ano = models.CharField(max_length=4, blank=True, null=True, default="")
    autor = models.CharField(max_length=400, blank=True, null=True, default="")
    resumo = models.CharField(max_length=500, blank=True, null=True, default="")
    palavras_chaves = models.CharField(max_length=350, blank=True, null=True, default="")
    categoria = models.CharField(max_length=120, choices=CATEGORIA)
    tipo = models.CharField(max_length=100, choices=TIPO)
    editora = models.CharField(max_length=300, blank=True, null=True, default="")
    orientador = models.CharField(max_length=500, blank=True, null=True, default="")
    uri = models.CharField(max_length=300, blank=True, null=True, default="")
    tipo_acesso = models.CharField(max_length=500, blank=True, null=True, default="")
    data_publicacao = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id

