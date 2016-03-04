# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_auto_20160303_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 3, 18, 38, 47, 835997), max_length=128),
        ),
    ]
