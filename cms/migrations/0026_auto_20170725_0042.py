# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20170725_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagesectioncontent',
            name='button_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepagesectioncontent',
            name='button_text',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]