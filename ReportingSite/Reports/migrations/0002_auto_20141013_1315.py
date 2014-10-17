# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_report',
            name='reporting_week',
            field=models.DateTimeField(verbose_name='reporting week'),
        ),
    ]
