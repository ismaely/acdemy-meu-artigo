"""/**
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2022-02-12 23:44:39
 * @modify date 2022-02-12 23:44:39
 */
"""

from django.shortcuts import render
from django.db.models import Count, Exists, Q
import sweetify
from app.models import Arquivo
from app.forms import Arquivo_Form
from pagina.forms import Pesquisa_Forms


def registar_arquivos(request):
    form = Arquivo_Form(request.POST or None)
    if request.method == "POST":
        form = Arquivo_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sweetify.success(request,'Arquivo Registado com sucesso!....', timer='4900', button='Ok')
            form = Arquivo_Form()
    #print(form.errors)
    context = {'form': form}
    return render (request, 'app/adicionar_arquivo.html', context)


def listar_arquivos(request):
    lista = Arquivo.objects.select_related().all().order_by('-titulo')
    context = {'lista':lista}
    return render (request, 'app/listar_arquivos.html', context)


def home(request):
    context = {}
    return render(request, 'app/home.html', context)



def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def service(request):
    context = {}
    return render(request, 'app/service.html', context)


def loginUser(request):
    context = {}
    return render(request, 'app/login.html', context)


def about_us(request):
    context = {}
    return render(request, 'app/about_us.html', context)


def pesquisar(request):
    form = Pesquisa_Forms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            titulo = form.cleaned_data.get('titulo')
            #resp = Profissao.objects.select_related('estudante').filter(Q(estudante__pessoa__bi__contains=bi) | Q(estudante__pessoa__passaporte=bi) | Q(estudante__numero_estudante__contains=bi) )
            lista = Arquivo.objects.select_related().filter(Q(titulo__contains=titulo)).all()
            context = {'form': form,'lista': lista}
            return render(request, 'app/pesquisar.html', context)
    
    context = {'form': form}
    return render(request, 'app/pesquisar.html', context)