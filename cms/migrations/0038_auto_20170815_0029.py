# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0037_auto_20170815_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteconfig',
            name='homepage',
        ),
        migrations.DeleteModel(
            name='WebsiteConfig',
        ),
    ]