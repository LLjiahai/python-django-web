# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=6)),
                ('url', models.CharField(max_length=50)),
                ('full_url', models.CharField(max_length=100)),
            ],
        ),
    ]