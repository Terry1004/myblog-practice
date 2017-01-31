# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20170127_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='blog_author',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='content',
            new_name='blog_content',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='blog_pub_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='comment_author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment_content',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='pub_date',
            new_name='comment_pub_date',
        ),
    ]
