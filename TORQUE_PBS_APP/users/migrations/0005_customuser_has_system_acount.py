# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_has_system_acount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='has_system_acount',
            field=models.BooleanField(default=False),
        ),
    ]
