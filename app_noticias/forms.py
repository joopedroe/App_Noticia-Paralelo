from django import forms
from django.forms import ModelForm

from .models import Noticia

class NoticiaForms(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','conteudo']
        #exclude = ['data_criacao','data_publicacao','publicado']
