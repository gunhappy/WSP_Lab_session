# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('middlename', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('dateofB', models.CharField(max_length=45)),
            ],
        ),
    ]
