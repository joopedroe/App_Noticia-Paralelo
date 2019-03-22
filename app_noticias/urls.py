from django.urls import path
from . import views
from app_noticias.views import *

urlpatterns=[
    path('',RetornaNoticia, name='home'),
    #path('todas/', get_cadastro, name='todas'),#cadastro via formulario, incompleto.
    path('pessoas/',PessoaFisica, name='pessoas'),
    path('cadastro/',get_cadastro, name='cadastro'),

]
