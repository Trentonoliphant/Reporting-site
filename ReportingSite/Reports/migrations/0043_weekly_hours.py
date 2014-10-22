# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0042_auto_20141021_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekly_hours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Hours', models.IntegerField(default=0)),
                ('Week_of', models.DateField(default=datetime.datetime(2014, 10, 21, 11, 16, 13, 448000), verbose_name=b'reporting week')),
                ('Employee', models.ForeignKey(to='Reports.Employee')),
                ('Project', models.ForeignKey(to='Reports.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
