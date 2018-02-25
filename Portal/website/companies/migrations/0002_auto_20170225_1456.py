# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='close',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='open',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ticker',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='volume',
        ),
        migrations.AddField(
            model_name='stock',
            name='data',
            field=models.TextField(blank=True, db_column='data'),
        ),
        migrations.AddField(
            model_name='stock',
            name='desc',
            field=models.TextField(default='Nothing Entered'),
        ),
    ]
