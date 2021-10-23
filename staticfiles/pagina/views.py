from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    context = {}
    return render(request, 'base.html', context)



def about(request):
    context = {}
    return render(request, 'pagina/about.html', context)
