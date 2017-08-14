# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_homepagesectioncontent_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselslide',
            name='sorting_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='homepagesection',
            name='sorting_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='homepagesectioncontent',
            name='sorting_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=models.ManyToManyField(blank=True, null=True, to='cms.HomepageSection'),
        ),
        migrations.AlterField(
            model_name='homepagesection',
            name='contents',
            field=models.ManyToManyField(blank=True, null=True, to='cms.HomepageSectionContent'),
        ),
    ]
