# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    # related name defines a name for the many-to-one relationship
    course = models.ForeignKey(Course, related_name='steps')

    class Meta:
        ordering = ['order',]
        # this specifies that together, these fields must create a unique key
        unique_together = ['title', 'course']

    def __str__(self):
        return self.title
