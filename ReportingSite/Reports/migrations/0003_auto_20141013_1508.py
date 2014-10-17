# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0002_auto_20141013_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weekly_report',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='weekly_report',
            name='project',
        ),
        migrations.AddField(
            model_name='employee',
            name='Weekly_report',
            field=models.ManyToManyField(to='Reports.Weekly_report'),
            preserve_default=True,
        ),
    ]
