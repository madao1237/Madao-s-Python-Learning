# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooAPI', '0002_auto_20161023_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actress',
            name='birth',
            field=models.DateTimeField(blank=True, verbose_name='Birthday'),
        ),
    ]
