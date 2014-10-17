# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0020_auto_20141014_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='Week_of',
            field=models.DateTimeField(verbose_name='reporting week', default=datetime.datetime(2014, 10, 14, 10, 27, 41, 865045)),
        ),
    ]
