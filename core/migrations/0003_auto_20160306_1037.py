# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160305_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='important',
            field=models.BooleanField(default=False, verbose_name=b'Show in summary'),
        ),
        migrations.AddField(
            model_name='question',
            name='short_title',
            field=models.CharField(default=b'', max_length=2000, verbose_name=b'Short  title', blank=True),
        ),
    ]
