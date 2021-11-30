from django.urls import path
from django.conf import settings
from . import views

app_name = 'pagina'
urlpatterns = [
    path('', views.index, name="index"),
    path('registar', views.registar, name="registar-se"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('service', views.service, name="service"),
    path('parceiros', views.parceiros, name="parceiros"),
    path('about', views.about_us, name="about_us"),
    path('resultado_pesquisa', views.resultado_pesquisa, name="resultado_pesquisa"),
]
