# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0011_remove_employee_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Project',
            field=models.ManyToManyField(to='Reports.Project'),
            preserve_default=True,
        ),
    ]
