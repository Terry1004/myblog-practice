# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=140),
        ),
    ]
