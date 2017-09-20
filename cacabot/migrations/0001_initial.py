# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaChatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userkey', models.CharField(max_length=20)),
                ('updatedate', models.DateTimeField(verbose_name='date published')),
                ('inputdate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='CaKeyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('updatedate', models.DateTimeField(verbose_name='date published')),
                ('inputdate', models.DateTimeField(verbose_name='date published')),
                ('friends', models.ManyToManyField(blank=True, related_name='_cakeyboard_friends_+', to='cacabot.CaKeyboard')),
            ],
        ),
        migrations.CreateModel(
            name='CaKeyfriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userkey', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('updatedate', models.DateTimeField(verbose_name='date published')),
                ('inputdate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='CaMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userkey', models.CharField(max_length=20)),
                ('msgtype', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=1024)),
                ('outmessage', models.CharField(max_length=1024)),
                ('keyboard', models.CharField(max_length=255)),
                ('updatedate', models.DateTimeField(verbose_name='date published')),
                ('inputdate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
