# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='next_if_no',
            field=models.IntegerField(default=0, verbose_name=b'Next If No', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='next_if_yes',
            field=models.IntegerField(default=0, verbose_name=b'Next If Yes', blank=True),
        ),
    ]
