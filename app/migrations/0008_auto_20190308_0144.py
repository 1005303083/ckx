# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-08 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='specifics',
            field=models.CharField(max_length=100),
        ),
    ]
