# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0039_auto_20141020_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='weekly_hours',
        ),
    ]
