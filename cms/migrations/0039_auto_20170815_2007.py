# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0038_auto_20170815_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='seo_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='seo_title',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='heading',
            field=models.CharField(max_length=100),
        ),
    ]
