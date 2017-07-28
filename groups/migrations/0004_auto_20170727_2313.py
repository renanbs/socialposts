# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20170725_0254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='group',
            name='contact_updated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
