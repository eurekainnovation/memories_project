# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0019_auto_20160314_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date',
            field=models.CharField(default=datetime.datetime(2016, 3, 16, 16, 5, 26, 840177), max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 16, 16, 5, 26, 841026), max_length=128),
        ),
    ]
