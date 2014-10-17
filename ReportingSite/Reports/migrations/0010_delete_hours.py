# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0009_auto_20141014_0945'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hours',
        ),
    ]
