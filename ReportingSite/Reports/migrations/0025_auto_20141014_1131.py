# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0024_auto_20141014_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(verbose_name='reporting week', default='October 14 2014'),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(verbose_name='reporting week', default=datetime.datetime(2014, 10, 14, 11, 31, 7, 95436)),
        ),
    ]
