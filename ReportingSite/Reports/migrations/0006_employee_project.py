# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0005_auto_20141013_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Project',
            field=models.ManyToManyField(to='Reports.Project'),
            preserve_default=True,
        ),
    ]
