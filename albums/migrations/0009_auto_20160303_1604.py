# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_auto_20160303_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='usr',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 3, 3, 16, 4, 53, 181324), max_length=128),
        ),
    ]
