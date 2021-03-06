# Generated by Django 2.1.7 on 2019-03-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0002_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data_criacao',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='data_publicacao',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='publicado',
            field=models.BooleanField(null=True),
        ),
    ]
