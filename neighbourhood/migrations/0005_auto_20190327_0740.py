# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0004_remove_business_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='image',
            field=models.ImageField(null=True, upload_to='Businessimage'),
        ),
    ]
