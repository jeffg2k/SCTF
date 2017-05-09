# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 16:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='users',
            field=models.ManyToManyField(through='accounts.UserProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]