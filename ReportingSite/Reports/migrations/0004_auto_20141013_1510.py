# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0003_auto_20141013_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Weekly_report',
        ),
        migrations.AddField(
            model_name='weekly_report',
            name='Employee',
            field=models.ManyToManyField(to='Reports.Employee'),
            preserve_default=True,
        ),
    ]
