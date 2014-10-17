# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0026_auto_20141014_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(verbose_name='reporting week', default=datetime.datetime(2014, 10, 14, 11, 32, 6, 969250)),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(verbose_name='reporting week', default=datetime.datetime(2014, 10, 14, 11, 32, 6, 970250)),
        ),
    ]
