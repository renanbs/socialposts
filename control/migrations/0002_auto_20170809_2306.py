# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='control',
            old_name='posts',
            new_name='post',
        ),
    ]
