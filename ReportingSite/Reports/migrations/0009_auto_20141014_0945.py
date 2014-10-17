# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0008_auto_20141014_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hours',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='hours',
            name='project',
        ),
    ]
