# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0036_auto_20141014_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='needed_hours',
            new_name='total_hours',
        ),
        migrations.RemoveField(
            model_name='project',
            name='employee',
        ),
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 16, 17, 2, 644210), verbose_name='reporting week'),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 16, 17, 2, 644210), verbose_name='reporting week'),
        ),
    ]
