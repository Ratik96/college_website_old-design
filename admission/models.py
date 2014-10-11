from django.db import models
from django import forms
from django.utils import timezone
import office
def get_hash(string):
		'''returns the hash of a string.
		length=56, sha224 implementation'''
		import hashlib
		return hashlib.sha224(string).hexdigest()
		
class dates(models.Model):
	'''
	The important dates related to admissions
	'''
	def __unicode__(self):
		return str(self.activity)
	date=models.DateField()
	activity=models.CharField(max_length=100)
	valid_upto=models.DateField()

class category(models.Model):
	'''
	stores the various quotas for admission
	'''
	def __unicode__(self):
		return str(self.code)
	name=models.CharField(max_length=50)
	code=models.CharField(max_length=5)
	
class cutoff_subject(models.Model):
	'''
	cutoffs for a course
	'''
	def __unicode__(self):
		return str(self.course.__unicode__())
	valid_upto=models.DateField()
	course=models.ForeignKey(office.models.course,related_name='course_for')
	
	
class category_cutoff(models.Model):
	'''
	stores cutoffs for a category
	'''
	category=models.ForeignKey(category,related_name='category')
	science=models.FloatField()
	commerce=models.FloatField(null=True,blank=True,default=None)
	humanities=models.FloatField(null=True,blank=True,default=None)
	cutoff_subject=models.ForeignKey(cutoff_subject,related_name='cutoff_subject')


class notice(models.Model):
	'''
	notice for admissions
	'''
	def __unicode__(self):
		return str(self.title)
	title=models.CharField(max_length=100)
	description=models.TextField()
	
	associated_file=models.FileField(upload_to='admissions/notice')
	
	publish_date=models.DateField(default=timezone.now())
class q_a(models.Model):
	'''
	question answer model.
	contains the question text along with answer text and a rank value.
	Rank is where the question is displayed
	'''
	question=models.TextField()
	answer=models.TextField()
	rank=models.SmallIntegerField()

