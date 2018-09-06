from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length =250)
	album_title = models.CharField(max_length=500)
	genre=models.CharField(max_length=1000)
	album_logo = models.CharField(max_length=1000)

	def get_absolute_url(self):
		return reverse('albums')


	def __str__(self):
		return self.artist

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	song_type= models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)

	def __str__(self):
		return self.song_title
 