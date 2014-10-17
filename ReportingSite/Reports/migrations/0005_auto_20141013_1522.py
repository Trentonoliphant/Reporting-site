# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0004_auto_20141013_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='weekly_hours',
            new_name='total_hours',
        ),
        migrations.AddField(
            model_name='weekly_report',
            name='Project',
            field=models.ManyToManyField(to='Reports.Project'),
            preserve_default=True,
        ),
    ]
