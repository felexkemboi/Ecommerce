from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length = 120)
	descriptions = models.TextField(default = 'descriptions default text')
	


	def __unicode__(self):
		return self.name

