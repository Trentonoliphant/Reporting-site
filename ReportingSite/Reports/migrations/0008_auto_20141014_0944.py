# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0007_auto_20141014_0943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='project',
            new_name='Project',
        ),
    ]
