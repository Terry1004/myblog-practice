# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170107_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=140)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Blog')),
                ('reply_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='account.Comment')),
            ],
        ),
    ]
