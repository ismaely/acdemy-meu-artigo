from django.contrib import admin
from pagina.models import Documenmto

# Register your models here.

class dispaly_Documento(admin.ModelAdmin):
    list_display = ('id','titulo','autor', 'ano', 'categoria', 'palavras_chaves')

admin.site.register(Documenmto, dispaly_Documento)