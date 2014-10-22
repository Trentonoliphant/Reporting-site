# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0041_auto_20141020_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_name',
            new_name='Employee_name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='Project_name',
        ),
        migrations.AddField(
            model_name='employee',
            name='Available_hours',
            field=models.IntegerField(default=40),
            preserve_default=True,
        ),
    ]
