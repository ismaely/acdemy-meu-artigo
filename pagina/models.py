from django.db import models

# Create your models here.

class Documenmto(models.Model):
    titulo = models.CharField(max_length=120, blank=True, null=True,default="")
    instituicao = models.CharField(max_length=120, blank=True, null=True,default="")
    ano = models.CharField(max_length=4, blank=True, null=True, default="")
    data_publicacao = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.id

