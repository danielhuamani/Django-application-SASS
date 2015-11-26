# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0006_auto_20150919_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.FileField(upload_to=b'imagen', verbose_name=b'imagen'),
        ),
    ]
