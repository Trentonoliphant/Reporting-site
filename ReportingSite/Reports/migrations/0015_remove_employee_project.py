# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0014_employee_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='project',
        ),
    ]
