# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0028_auto_20170725_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagesectioncontent',
            name='width',
            field=models.IntegerField(default=4),
        ),
    ]
