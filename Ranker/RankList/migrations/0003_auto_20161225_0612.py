# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-25 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankList', '0002_auto_20161225_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bestcoder_rating',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='codeforces_rating',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='hdu_problems',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='poj_problems',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vj_problems',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
