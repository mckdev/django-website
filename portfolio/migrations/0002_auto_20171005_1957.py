# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-05 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioitem',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='featured_image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='portfolio_featured'),
        ),
    ]