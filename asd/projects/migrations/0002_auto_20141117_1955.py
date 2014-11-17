# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='rate',
            field=models.IntegerField(verbose_name=b'Rate'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.IntegerField(verbose_name=b'Price'),
            preserve_default=True,
        ),
    ]
