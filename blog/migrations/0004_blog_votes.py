# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-03 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u8d5e\u6b21\u6570'),
        ),
    ]