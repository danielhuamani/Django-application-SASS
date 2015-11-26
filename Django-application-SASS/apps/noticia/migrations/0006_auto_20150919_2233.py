# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0005_noticia_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.FileField(upload_to=b'media', verbose_name=b'imagen'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=120, verbose_name=b'Titulo'),
        ),
    ]
