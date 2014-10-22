# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0043_weekly_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_hours',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 21, 11, 20, 10, 775000), verbose_name=b'reporting week'),
        ),
    ]
