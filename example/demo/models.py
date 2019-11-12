# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FooModel(models.Model):
    text = models.CharField(
        max_length=100, default="", null=True, help_text="Text for foo"
    )


class BarModel(models.Model):
    text = models.CharField(
        max_length=100, default="", null=True, help_text="Text for bar"
    )
