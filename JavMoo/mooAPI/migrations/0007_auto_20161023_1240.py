# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooAPI', '0006_auto_20161023_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='actress',
            name='avatar',
            field=models.URLField(blank=True, default='', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='\u5e74\u9f84'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='bust',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='\u80f8\u56f4'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u51fa\u751f\u5730'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='cup',
            field=models.CharField(blank=True, default='0', max_length=1, verbose_name='\u7f69\u676f'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='\u8eab\u9ad8'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='hips',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='\u81c0\u56f4'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='hoby',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u7231\u597d'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='uuid',
            field=models.CharField(default='-1', max_length=100, verbose_name='uuid'),
        ),
        migrations.AlterField(
            model_name='actress',
            name='waist',
            field=models.PositiveSmallIntegerField(blank=True, default='0', verbose_name='\u8170\u56f4'),
        ),
    ]