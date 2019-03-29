from django import forms
from django.forms import ModelForm

from .models import *

class PessoaForms(ModelForm):
    class Meta:
        model=Pessoa
        fields=['usuario','nome','cpf','dataNascimento','telefone_celular','telefone_fixo','email']
        widgets = {
            'dataNascimento' : forms.DateInput ( format = ' % d /% m /% y ' )
        }

class TagsForms(ModelForm):
    class Meta:
        model= Tag
        fields= ['nome','slug']

class NoticiaForms(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo','conteudo','autor','tags','data_criacao']
        exclude = ['data_publicacao','publicado']

class UserForms(ModelForm):
    class Meta:
        model=User
        fields=['username','password']




