from django.db import models

class Noticia(models.Model):
    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural= 'Notícias'

    titulo=models.CharField('título', max_length=128)
    conteudo= models.TextField()
    data_criacao=models.DateTimeField(null=True)
    data_publicacao=models.DateTimeField(null=True)
    publicado=models.BooleanField(null=True)

class Pessoa(models.Model):
    class Meta:
        verbose_name='Pessoa'
        verbose_name_plural='Pessoas'
    
    nome=models.CharField('Nome',max_length=128)
    cpf=models.CharField('Cpf',max_length=11)
    dataNascimento=models.DateField('Data de Nascimento')