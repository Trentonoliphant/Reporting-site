# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0035_auto_20141014_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='total_hours',
            new_name='needed_hours',
        ),
        migrations.AlterField(
            model_name='hours_report',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 16, 13, 38, 173031), verbose_name='reporting week'),
        ),
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateField(default=datetime.datetime(2014, 10, 14, 16, 13, 38, 174031), verbose_name='reporting week'),
        ),
    ]
