# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=120, verbose_name=b'Codigo')),
                ('estado', models.CharField(default=b'P', max_length=120, verbose_name=b'Estado', choices=[(b'P', b'PUBLICADO'), (b'R', b'REVISADO')])),
                ('fecha', models.DateField(auto_now=True, verbose_name=b'Fecha')),
                ('imagen', models.ImageField(upload_to=b'imagen', verbose_name=b'imagen')),
                ('contenido', models.TextField(verbose_name=b'Contenido')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
