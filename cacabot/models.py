# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class CaKeyboard(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    friends = models.ManyToManyField('self', blank=True)
    updatedate = models.DateTimeField('date published')
    inputdate = models.DateTimeField('date published')

@python_2_unicode_compatible
class CaMessage(models.Model):
    userkey = models.CharField(max_length=20)
    msgtype = models.CharField(max_length=10)
    message = models.CharField(max_length=1024)
    outmessage = models.CharField(max_length=1024)
    keyboard = models.CharField(max_length=255)
    updatedate = models.DateTimeField('date published')
    inputdate = models.DateTimeField('date published')


@python_2_unicode_compatible
class CaKeyfriend(models.Model):
    userkey = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    updatedate = models.DateTimeField('date published')
    inputdate = models.DateTimeField('date published')


@python_2_unicode_compatible
class CaChatroom(models.Model):
    userkey = models.CharField(max_length=20)
    updatedate = models.DateTimeField('date published')
    inputdate = models.DateTimeField('date published')
    #objects = CacabotManager()   #임의로 추가함
