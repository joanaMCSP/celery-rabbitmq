# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('map_url', 'map_url'), ('merge_maps', 'merge_maps')], max_length=20)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('started', 'started'), ('finished', 'finished'), ('failed', 'failed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('argument', models.TextField()),
                ('result', models.TextField(blank=True)),
            ],
        ),
    ]