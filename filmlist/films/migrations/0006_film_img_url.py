# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-20 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_theater_films'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='img_url',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
