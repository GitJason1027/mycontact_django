# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ABook', '0003_userinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
