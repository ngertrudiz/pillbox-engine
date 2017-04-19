# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-19 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='last_unzipped',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Last Unzipped'),
        ),
        migrations.AlterField(
            model_name='source',
            name='last_downloaded',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Last Downloaded'),
        ),
    ]