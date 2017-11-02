# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 17:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0005_auto_20171102_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='user',
            field=models.OneToOneField(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
