# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    todoDate = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)


def _str_(self):
    return self.title
