# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0016_auto_20160305_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.CharField(unique=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 6, 9, 45, 32, 86118), max_length=128),
        ),
    ]
