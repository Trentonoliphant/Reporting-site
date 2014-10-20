# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0038_auto_20141014_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hours_report',
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='hours_report',
            name='Project',
        ),
        migrations.DeleteModel(
            name='Hours_report',
        ),
        migrations.RemoveField(
            model_name='weekly_report',
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='weekly_report',
            name='Project',
        ),
        migrations.DeleteModel(
            name='Weekly_report',
        ),
        migrations.AddField(
            model_name='project',
            name='Employee_list',
            field=models.ManyToManyField(to='Reports.Employee'),
            preserve_default=True,
        ),
    ]
