# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_homepage_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagesectioncontent',
            name='width',
            field=models.IntegerField(default=3),
        ),
    ]