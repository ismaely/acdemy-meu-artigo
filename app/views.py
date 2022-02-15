"""/**
 * @author [Gunza Ismael]
 * @email [7ilip@gmail.com]
 * @create date 2022-02-12 23:44:39
 * @modify date 2022-02-12 23:44:39
 */
"""

from django.shortcuts import render
from django.db.models import Count, Exists, Q




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
    context = {}
    return render(request, 'app/pesquisar.html', context)