from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'pagina/index.html', context)



def registar(request):
    context = {}
    return render(request, 'pagina/registar.html', context)


def loginUser(request):
    context = {}
    return render(request, 'pagina/sign.html', context)
