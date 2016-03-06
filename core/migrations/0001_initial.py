# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=b'', max_length=2000, verbose_name=b'Question', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'images/authors/', blank=True)),
            ],
        ),
    ]
