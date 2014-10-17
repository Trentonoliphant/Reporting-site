# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0031_auto_20141014_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 11, 37, 4, 232349), verbose_name='reporting week'),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 11, 37, 4, 232349), verbose_name='reporting week'),
        ),
    ]
