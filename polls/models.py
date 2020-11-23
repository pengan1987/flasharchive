# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FlashAnim(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    chinese_name = models.CharField(max_length=128, blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    english_name = models.CharField(max_length=128, blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    edit_permission = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'flash'
