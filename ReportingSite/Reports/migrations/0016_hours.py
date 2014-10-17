# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0015_remove_employee_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Employee', models.ForeignKey(to='Reports.Employee')),
                ('Project', models.ForeignKey(to='Reports.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
