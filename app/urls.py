from django.urls import path
from django.conf import settings
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name="index"),
    path('servicos', views.service, name="servicos"),
    path('login', views.loginUser, name="login"),
    path('about_us', views.about_us, name="about-us"),
    path('pesquisar', views.pesquisar, name="pesquisar"),
    path('home', views.home, name="home"),
    path('registar_arquivos', views.registar_arquivos, name="registar-arquivos"),
    path('listar_arquivos', views.listar_arquivos, name="listar-arquivos"),
   
   
]
