# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jizhang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='金额'),
        ),
    ]
