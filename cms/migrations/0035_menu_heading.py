# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_auto_20170814_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='heading',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
