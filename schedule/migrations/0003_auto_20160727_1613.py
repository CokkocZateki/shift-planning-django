# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20160727_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='workgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Workplace'),
        ),
    ]