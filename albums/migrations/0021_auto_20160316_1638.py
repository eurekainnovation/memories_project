# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0020_auto_20160316_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.CharField(default=datetime.datetime(2016, 3, 16, 16, 38, 16, 869594), max_length=128),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 16, 16, 38, 16, 870427), max_length=128),
        ),
    ]
