# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
