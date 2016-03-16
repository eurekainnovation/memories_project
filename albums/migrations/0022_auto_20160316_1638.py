# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0021_auto_20160316_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 16, 38, 50, 461370), blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 16, 16, 38, 50, 462202), max_length=128),
        ),
    ]
