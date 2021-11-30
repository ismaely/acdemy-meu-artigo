from django import forms
from django.forms import ModelForm
from core.opcoes import CATEGORIA, TIPO

class Pesquisa(forms.Form):
    categoria = forms.CharField(widget=forms.Select(choices=CATEGORIA, attrs={'class': 'form-control'}))
    tipo = forms.CharField(widget=forms.Select(choices=TIPO, attrs={'class': 'form-control'}))
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control maiuscula'}))
