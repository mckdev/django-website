# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='name',
        ),
    ]
