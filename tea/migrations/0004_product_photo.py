# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0003_auto_20160727_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='DSC_0141.JPG', upload_to='/static/images/products_photo/'),
        ),
    ]
