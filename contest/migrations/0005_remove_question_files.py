# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 03:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_question_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='files',
        ),
    ]
