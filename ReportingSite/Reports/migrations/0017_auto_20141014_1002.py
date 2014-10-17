# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0016_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='hours',
            name='Hours',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hours',
            name='Week_of',
            field=models.DateTimeField(verbose_name='reporting week', default=datetime.datetime(2014, 10, 14, 10, 2, 31, 179815)),
            preserve_default=True,
        ),
    ]
