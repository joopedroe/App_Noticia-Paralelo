from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect

from .forms import *
from .models import Noticia, Pessoa

class HomePageView(ListView):
    model=Noticia
    model1=Pessoa
    template_name='app_noticias/home.html'
    
class InicioView(TemplateView):
    template_name='app_noticias/inicial.html'
# Create your views here.

def PessoaFisica(request):
    noticias=Noticia.objects.all()
    pessoas=Pessoa.objects.all()
    return render(request,'app_noticias/home.html',{'pessoas':pessoas, 'noticias':noticias})

def RetornaNoticia(request):
    noticias=Noticia.objects.all()
    return render(request,'app_noticias/home.html',{'noticias':noticias})
 
def get_cadastro(request):
    if request.method == "POST":
        form=NoticiaForms(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('home')
    else:
        form=NoticiaForms()
    return render (request,'app_noticias/inicial.html',{'form':form})

def get_cadastroAutor(request):
    if request.method == "POST":
        form=PessoaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoas')
    else:
        form=PessoaForms()
    return render (request,'app_noticias/pessoa.html',{'form':form})

def get_cadastroTags(request):
    if request.method == 'POST':
        form=TagsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoas')
    else:
        form=TagsForms()
    return render (request, 'app_noticias/tags.html',{'form':form})

def get_cadastroUser(request):
    if request.method == 'POST':
        form=UserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserForms()
    return render (request, 'app_noticias/usuario.html',{'form':form})