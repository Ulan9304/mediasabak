# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0004_auto_20171219_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_models.Test', verbose_name='Выберите тест'),
        ),
        migrations.AddField(
            model_name='test',
            name='correct',
            field=models.CharField(blank=True, max_length=500, verbose_name='right answer message'),
        ),
        migrations.AddField(
            model_name='test',
            name='incorrect',
            field=models.CharField(blank=True, max_length=500, verbose_name='wrong answer message'),
        ),
    ]