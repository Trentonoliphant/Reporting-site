# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0006_employee_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hours',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('employee', models.ForeignKey(to='Reports.Employee')),
                ('project', models.ForeignKey(to='Reports.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Project',
            new_name='project',
        ),
    ]
