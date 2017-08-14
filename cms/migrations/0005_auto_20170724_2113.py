# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20170724_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='carousel',
            name='slides',
            field=models.ManyToManyField(to='cms.Slide'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='carousel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Carousel'),
        ),
    ]
