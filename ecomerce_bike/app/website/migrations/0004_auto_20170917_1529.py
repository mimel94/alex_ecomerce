# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170917_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='photo',
            field=models.ImageField(default='media/None/no-img.png', upload_to='motos/', verbose_name='Foto'),
        ),
    ]
