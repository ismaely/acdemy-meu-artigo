from django import forms
from django.forms import ModelForm
from app.models import Arquivo


class Arquivo_Form(ModelForm):
    class Meta:
        arquivo = forms.FileField()
        model = Arquivo
        fields = ['titulo', 'autor', 'numero_pagina', 'tipologia', 'data', 'arquivo','descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_pagina': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.TextInput(attrs={'type':'date', 'class': 'form-control'}),
            'tipologia': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

