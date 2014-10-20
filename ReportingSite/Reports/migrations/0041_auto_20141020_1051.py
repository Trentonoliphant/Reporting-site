# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0040_remove_employee_weekly_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Employee_list',
            new_name='Employee',
        ),
    ]
