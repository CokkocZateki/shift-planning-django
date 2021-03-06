# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('personal_number', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('main_workplace', models.CharField(max_length=50)),
                ('work_area', models.CharField(choices=[('DS', 'Downstairs'), ('US', 'Upstairs')], default='DS', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('competence', models.IntegerField()),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Employee')),
            ],
            options={
                'ordering': ['competence'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('workers', models.ManyToManyField(through='schedule.Membership', to='schedule.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='workgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.WorkPlace'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Question'),
        ),
    ]
