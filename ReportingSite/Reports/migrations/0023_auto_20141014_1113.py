# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0022_auto_20141014_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours_report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Hours', models.IntegerField(default=0)),
                ('Week_of', models.DateField(default=datetime.datetime(2014, 10, 14, 11, 13, 28, 643818), verbose_name='reporting week')),
                ('Employee', models.ForeignKey(to='Reports.Employee')),
                ('Project', models.ForeignKey(to='Reports.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='hours',
            name='Employee',
        ),
        migrations.RemoveField(
            model_name='hours',
            name='Project',
        ),
        migrations.DeleteModel(
            name='Hours',
        ),
    ]
