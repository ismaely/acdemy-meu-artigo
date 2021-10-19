from django.urls import path
from django.conf import settings
from . import views

app_name = 'pagina'
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="adicionar-Inscricao"),
]
