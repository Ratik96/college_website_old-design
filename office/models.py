from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import *

from django.core.urlresolvers import reverse

import datetime


class course_type(models.Model):
	'''
	The types of courses available in the college.
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	
	
class course(models.Model):
	'''
	Defines the courses available in college
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	course_type=models.ForeignKey(course_type,related_name='course_type')
	description=models.TextField(default='',blank=True)#description of the course
	def get_absolute_url(self):
		return reverse('course_detail',args=[self.id])
class paper(models.Model):
	'''
	Describes a paper that is taught in college.
	Each paper has an associated course.
	'''
	def __unicode__(self):
		return self.code
	code=models.CharField('The paper code',max_length=10)
	name=models.CharField('The name of paper',max_length=25)
	course=models.ForeignKey(course)
	semester=models.IntegerField('The semester in which the paper appears',default=0)	
class deptsoc(models.Model):
	'''
	Describes the various departments and societies in college.
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=35)
	nickname=models.CharField(max_length=10,unique=True)#nickname for url
	logo=models.ImageField(upload_to='deptsoc_logos',blank=True,null=True)
	
	description=models.TextField(blank=True)
	founding_date=models.DateField('The founding date of the society/department',default=timezone.now())
	
	#society related stuff
	is_society=models.BooleanField(default=False)
	
	def get_absolute_url(self):
		if self.is_society:
			return reverse('society_detail',args=[self.nickname])
		else:
			return reverse('department_detail',args=[self.nickname])
	
	
class profile(models.Model):
	'''
	The various attributes of the staff.
	Each associated with a user id.
	'''
	def __unicode__(self):
		return str(self.title)+' '+str(self.user.first_name)+' '+str(self.user.last_name)
	user=models.OneToOneField(User)
	nickname=models.CharField(max_length=10,unique=True)#for url
	title=models.CharField('Titles like Mr.',max_length=50,default='M.')
	picture=models.ImageField('The profile picture of the senior member',upload_to='userpics',default=None)
	def get_absolute_url(self):
		return reverse('profile_detail',args=[self.nickname])
	def thumbnail(self):
	        if self.picture:
	        	addr=self.picture.url
	        	addr.strip('/')
	                return u'<img src="'+addr+'" width=60 height=60 />'
	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True
		
class student(profile):
	'''
	Students in college
	'''
	course=models.ForeignKey(course,related_name='course')
	current_semester=models.SmallIntegerField(default=1)
	
	admission_date=models.DateField(default=timezone.now())
class faculty(profile):
	'''
	Faculty of college
	'''
	dept=models.ForeignKey(deptsoc,limit_choices_to={'is_society':False},related_name='dept')
	qualification=models.CharField(max_length=100,blank=True)
