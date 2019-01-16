# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 70)
    score = models.FloatField()
