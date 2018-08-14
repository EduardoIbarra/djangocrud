# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	genre = models.CharField(max_length=200)
	year = models.IntegerField()
	duration = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
	return '%s %s %s %s %s %s' (self.name, self.description, self.genre, self.year, self.duration, self.created_at)
