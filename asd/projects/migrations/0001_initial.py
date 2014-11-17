# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=255, verbose_name=b'Last name')),
                ('first_name', models.CharField(max_length=255, verbose_name=b'First name')),
                ('middle_name', models.CharField(max_length=255, verbose_name=b'Middle name')),
                ('birthday', models.DateField(verbose_name=b'Birthday')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name=b'Title')),
                ('rate', models.DecimalField(verbose_name=b'Rate', max_digits=3, decimal_places=3)),
            ],
            options={
                'verbose_name_plural': 'Positions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Procurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_amount', models.IntegerField(verbose_name=b'Work amount')),
                ('start_date', models.DateField(verbose_name=b'Start date')),
                ('planned_end_date', models.DateField(verbose_name=b'Planned end date')),
                ('real_end_date', models.DateField(null=True, verbose_name=b'Real end date')),
                ('employee', models.ForeignKey(verbose_name=b'Employee', to='projects.Employee')),
            ],
            options={
                'verbose_name_plural': 'Procurances',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255, verbose_name=b'Title')),
                ('deadline', models.DateField(verbose_name=b'Deadline')),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=3, decimal_places=3)),
                ('details', models.TextField(verbose_name=b'Details')),
                ('manager', models.ForeignKey(verbose_name=b'Manager', to='projects.Employee')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
            ],
            options={
                'verbose_name_plural': 'Project types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'Title')),
            ],
            options={
                'verbose_name_plural': 'Works',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(verbose_name=b'Project type', to='projects.ProjectType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='procurance',
            name='project',
            field=models.ForeignKey(verbose_name=b'Project', to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='procurance',
            name='work',
            field=models.ForeignKey(verbose_name=b'Work', to='projects.Work'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(verbose_name=b'Position', to='projects.Position'),
            preserve_default=True,
        ),
    ]
