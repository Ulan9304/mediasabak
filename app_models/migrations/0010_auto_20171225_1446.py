# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-25 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0009_remove_lesson_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='file',
            new_name='pdf_file',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='file2',
            new_name='word_file',
        ),
    ]
