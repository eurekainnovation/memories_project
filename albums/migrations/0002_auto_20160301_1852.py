# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='gallery',
        ),
        migrations.AddField(
            model_name='gallery',
            name='albums',
            field=models.ForeignKey(to='albums.Album', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gallery',
            name='contributor',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='usr',
            field=models.ForeignKey(to='albums.User', null=True),
        ),
    ]
