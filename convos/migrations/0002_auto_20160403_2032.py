# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('convos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convopage',
            name='picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_upload.picture'),
        ),
    ]