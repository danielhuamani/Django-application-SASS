# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0008_auto_20150919_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='estado',
            field=models.CharField(max_length=120, default='P', verbose_name='Estado', choices=[('P', 'PUBLICADO'), ('R', 'REVISADO')]),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateField(verbose_name='Fecha', auto_now=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(verbose_name='imagen', upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=120, verbose_name='Titulo'),
        ),
    ]
