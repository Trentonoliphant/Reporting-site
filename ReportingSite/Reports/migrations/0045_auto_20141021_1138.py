# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0044_auto_20141021_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_hours',
            name='Week_of',
            field=models.DateField(default=datetime.datetime(2014, 10, 21, 11, 38, 10, 738000), verbose_name=b'reporting week'),
        ),
    ]
