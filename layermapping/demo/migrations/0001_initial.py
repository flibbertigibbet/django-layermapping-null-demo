# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-11 22:06
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoGeoModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326)),
                ('fill_color', models.CharField(max_length=20)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('fill_opacity', models.FloatField()),
                ('some_number', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
