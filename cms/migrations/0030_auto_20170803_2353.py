# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_auto_20170725_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesection',
            name='hide_title',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homepagesectioncontent',
            name='hide_title',
            field=models.BooleanField(default=False),
        ),
    ]
