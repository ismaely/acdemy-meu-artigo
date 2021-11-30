from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from pagina.forms import Pesquisa_Forms

# Create your views here.

def index(request):
    form = Pesquisa_Forms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            tipo = form.cleaned_data.get('tipo')
            titulo = form.cleaned_data.get('titulo')
            context = {}
            return render(request, 'pagina/resultado_pesquisa.html', context)
    context = {'form': form}
    return render(request, 'pagina/index.html', context)


def resultado_pesquisa(request):
    form = Pesquisa_Forms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            tipo = form.cleaned_data.get('tipo')
            titulo = form.cleaned_data.get('titulo')
            context = {}
            return render(request, 'pagina/resultado_pesquisa.html', context)
    context = {'form': form}
    return render(request, 'pagina/resultado_pesquisa.html', context)


def about_us(request):
    context = {}
    return render(request, 'pagina/about.html', context)


def registar(request):
    context = {}
    return render(request, 'pagina/registar.html', context)


def loginUser(request):
    context = {}
    return render(request, 'pagina/sign.html', context)



def service(request):
    context = {}
    return render(request, 'pagina/service.html', context)


def parceiros(request):
    context = {}
    return render(request, 'pagina/parceiros.html', context)