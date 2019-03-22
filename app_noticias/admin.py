from django.contrib import admin

from .models import Noticia, Pessoa

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass