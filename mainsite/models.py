from django.db import models
from django.core.urlresolvers import reverse
from django import forms
from django.utils import timezone
import datetime
import random

class photo(models.Model):
	'''
	Abstract class to provide common attributes for photo data
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField('Name of the photo',max_length=40)
	associated_photo=models.ImageField('The associated image',upload_to='photos/hompage_slideshow/%Y/%m/%d')
	class Meta:
		abstract=True
	def thumbnail(self):
	        if self.associated_photo:
	        	addr=self.associated_photo.url
	        	addr.strip('/')
	                return u'<img src="'+addr+'" width=60 height=60 />'
	        else:
	        	return u'No image file found'
	thumbnail.short_description ='Thumbnail'
	thumbnail.allow_tags=True
	
class home_slideshow_photo(photo):
	'''
	Photos for homepage slideshow
	'''
	description=models.CharField('A description associated with the photo',max_length=50,blank=True,default='')
	
class notification(models.Model):
	'''
	The notifications to be uploaded to the website.
	'''

	title=models.CharField('The title of the notice',max_length=50)
	support_file1=models.FileField('The associated file with this document',upload_to='notification',blank=True,null=True,default=None)
	support_file2=models.FileField('The associated file with this document',upload_to='notification',blank=True,null=True,default=None)
	support_file3=models.FileField('The associated file with this document',upload_to='notification',blank=True,null=True,default=None)


	description=models.TextField('A description of the notification')
	publish_date=models.DateField(default=timezone.now())
	principal=models.BooleanField("Is is from the principal's desk",default=False)
	pinned=models.BooleanField('If this notification is to be permanently pinned on the homepage.',default=False)
	def recent(self):
		'''Checks if the record is one month old? Returns true if less than one month old.'''
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,20,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False
	recent.admin_order_field='publish_date'
	recent.boolean=True
	recent.short_description='Was published in last one month?'
	def get_absolute_url(self):
		return reverse('notice_detail',args=[self.id])

class Slot(models.Model):
	notif=models.ForeignKey(notification,related_name='notification')
	order=models.SmallIntegerField(default=1)
	text=models.TextField(blank=True)
	picture=models.ImageField(upload_to='notification/%y/%m/%d',blank=True,null=True,default=None)
	associated_file=models.FileField(upload_to='notification/%y/%m/%d',blank=True,null=True,default=None)
	link=models.CharField(max_length=400,blank=True)
	
class archives(models.Model):
	'''
	Archives for the college
	'''
	pass
