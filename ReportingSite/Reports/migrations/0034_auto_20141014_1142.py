# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0033_auto_20141014_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekly_report',
            name='report_name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 11, 42, 38, 186096), verbose_name='reporting week'),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 11, 42, 38, 187097), verbose_name='reporting week'),
        ),
    ]
