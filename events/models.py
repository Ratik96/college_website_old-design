from django.db import models
from django import forms
from office.models import society

class Location(models.Model):
	'''
	Locations where events need to be booked
	'''
	name=models.CharField(max_length=40)
	additional_info=models.TextField(blank=True)
	
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
	description=models.TextField(blank=True)
	organizer=models.ForeignKey(society)#who has organized this
	start=models.DateTimeField()
	end=models.DateTimeField()
		
class Schedule(models.Model):
	'''Schedule for an event
	'''
	title=models.CharField(max_length=50)
	description=models.TextField(blank=True)
	location=models.ForeignKey(Location,related_name='location')
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
