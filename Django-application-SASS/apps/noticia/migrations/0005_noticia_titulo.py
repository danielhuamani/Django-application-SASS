# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0004_auto_20150919_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(default=b'P', max_length=120, verbose_name=b'Titulo', choices=[(b'P', b'PUBLICADO'), (b'R', b'REVISADO')]),
        ),
    ]
