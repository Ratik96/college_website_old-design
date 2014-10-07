from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import *
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
	
class department(models.Model):
	'''
	Describes the various departments in college.
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=35)
	
class qualification(models.Model):
	'''
	Qualification for senior members
	'''
	def __unicode__(self):
		return str(self.q_type)+str(self.name)
	name=models.CharField('What topic or subject it is held in',max_length=50)
	q_type=models.CharField('The type of qualification',max_length=10)
	
class profile(models.Model):
	'''
	The various attributes of the staff.
	Each associated with a user id.
	'''
	def __unicode__(self):
		return str(self.title)+' '+str(self.user.firstname)+' '+str(self.user.lastname)
	user=models.OneToOneField(User)
	title=models.CharField('Titles bestowed on the senior member',max_length=50,default='M.')
	picture=models.ImageField('The profile picture of the senior member',upload_to='userpics',default=None)
	
	dept=models.ForeignKey(department,related_name='dept')
	joining_date=models.DateField('joining date of the senior member',default=timezone.now())
	
	qualifications=models.ManyToManyField(qualification)
	def thumbnail(self):
	        if self.picture:
	        	addr=self.picture.url
	        	addr.strip('/')
	                return u'<img src="'+addr+'" width=60 height=60 />'
	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True
	
class society(models.Model):	
	'''
	Describes the societies in college
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField('The society name',max_length=50)
	founding_date=models.DateField('The founding date of the society')
	staff_advisor=models.ForeignKey(profile,related_name='staff_advisor')
	
class student(models.Model):
	'''
	Students in college
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=40)
	picture=models.ImageField('Picture of the student',upload_to='studentpics')
	
	email=models.EmailField('The email of the student')
	
	course=models.ForeignKey(course,related_name='course')
	admission_date=models.DateField(default=timezone.now())
	def thumbnail(self):
	        if self.picture:
      	        	addr=self.picture.url
	        	addr.strip('/')
	                return u'<img src="'+addr+'" width=60 height=60 />'

	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True
