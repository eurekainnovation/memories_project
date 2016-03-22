# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0022_auto_20160316_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 23, 59, 53, 177000), blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 21, 23, 59, 53, 178000), max_length=128),
        ),
    ]
