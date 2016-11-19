# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-08 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Genre'),
        ),
    ]
