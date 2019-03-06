# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picapp', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picapp.Category'),
        ),
    ]
