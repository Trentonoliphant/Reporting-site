# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0019_auto_20141014_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='Employee',
            field=models.ForeignKey(to='Reports.Employee'),
        ),
        migrations.AlterField(
            model_name='hours',
            name='Week_of',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 14, 10, 17, 36, 702126), verbose_name='reporting week'),
        ),
    ]
