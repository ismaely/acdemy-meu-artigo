from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from pagina.models import Documenmto
from pagina.forms import Pesquisa_Forms
from django.db.models import Count, Exists, Q

# Create your views here.

def index(request):
    form = Pesquisa_Forms(request.POST or None)
   
    context = {'form': form}
    return render(request, 'pagina/index.html', context)


def resultado_pesquisa(request):
    form = Pesquisa_Forms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            categoria = form.cleaned_data.get('categoria')
            tipo = form.cleaned_data.get('tipo')
            titulo = form.cleaned_data.get('titulo')
            #resp = Profissao.objects.select_related('estudante').filter(Q(estudante__pessoa__bi__contains=bi) | Q(estudante__pessoa__passaporte=bi) | Q(estudante__numero_estudante__contains=bi) )
            lista = Documenmto.objects.select_related().filter(Q(titulo__contains=titulo) | Q(categoria=categoria) | Q(tipo=tipo)).all()
            context = {'form': form,'lista': lista}
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
    form = Pesquisa_Forms(request.POST or None)
   
    context = {'form': form}
    return render(request, 'pagina/service.html', context)


def parceiros(request):
    form = Pesquisa_Forms(request.POST or None)
   
    context = {'form': form}
    return render(request, 'pagina/parceiros.html', context)