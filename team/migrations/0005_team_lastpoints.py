# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170122_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='lastpoints',
            field=models.DateTimeField(null=True),
        ),
    ]
