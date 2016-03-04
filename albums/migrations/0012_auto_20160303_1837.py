# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_auto_20160303_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(default=datetime.date(2016, 3, 3)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 3, 18, 37, 7, 446001), max_length=128),
        ),
    ]
