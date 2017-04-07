# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatefitbackend', '0002_auto_20170322_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, default='2017-04-07 13:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='modified_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, default='2017-04-07 13:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='modified_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
