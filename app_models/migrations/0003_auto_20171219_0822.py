# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0002_auto_20171219_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app_models.LessonCategory'),
        ),
    ]