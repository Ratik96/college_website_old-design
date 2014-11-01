from django.db import models
from django import forms


class Location(models.Model):
	'''
	Locations where events need to be booked
	'''
	name=models.CharField(max_length=40)
	projector=models.BooleanField(default=False)#has projector
	ac=models.BooleanField(default=False)#has ac
	lights=models.BooleanField(default=False)#has lights
	board=models.BooleanField(default=True)#has black/white board

class Event(models.Model):
	'''
	Event in college
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField(max_length=40)
	
class Schedule(models.Model):
	'''Schedule for an event
	'''
	title=models.CharField(max_length=50)
	description=models.TextField(blank=True)
	location=models.ForeignKey(Location,related_name='location'3)
	start=models.DateTimeField()
	end=models.DateTimeField()
	event=models.ForeignKey(Event,related_name='event')
	

class Poster(models.Model):
	'''
	Posters for event
	'''
	associated_picture=models.ImageField(upload_to='events/posters/%y/%m/%d')
	event=models.ForeignKey(Event)
class Photos(models.Model):
	'''
	Photos of events
	'''
	associated_photo=models.ImageField(upload_to='events/photos/%y/%m/%d')
	event=models.ForeignKey(Event)
