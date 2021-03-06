# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0023_auto_20160321_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 22, 0, 46, 20, 384000), blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 22, 0, 46, 20, 385000), max_length=128),
        ),
    ]
