# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ver1', '0003_auto_20160522_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(blank=True, max_length=2, null=True, unique=True, verbose_name='Size Name'),
        ),
    ]
