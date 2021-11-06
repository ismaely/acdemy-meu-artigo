from django.db import models

# Create your models here.

class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=60, blank=True, null=True, default=" ")
    localizacao = models.CharField(max_length=60, blank=True, null=True, default=" ")
    sigla = models.CharField(max_length=60, blank=True, null=True, default=" ")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logo/%Y/', blank=True, null=True, default="dip.jpg")

    def __str__(self):
        return "%s" % (self.nome)