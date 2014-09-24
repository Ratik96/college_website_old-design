from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class document(models.Model):
	'''
	Abstract class to contain the common things needed for notices etc.
	Basic document attributes.
	
	'''
	def __unicode__(self):
		return self.title
	title=models.CharField('The title of the document',max_length=50)
	associated_file=models.FileField('The associated file with this document',upload_to='document')
	alive=models.BooleanField('Is this document available for public use?',default=True)
	class Meta:
		abstract=True
class photo(models.Model):
	'''
	Abstract class to provide common attributes for photo data
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField('Name of the photo',max_length=40)
	associated_photo=models.ImageField('The associated image',upload_to='photos/%Y/%m/%d')
	alive=models.BooleanField('Is this photo available for public use?',default=True)
	class Meta:
		abstract=True
	
			
class notification(document):
	'''
	The notifications to be uploaded to the website.
	'''
	description=models.TextField('A description of the notification')
	publish_date=models.DateField(default=timezone.now())
	pinned=models.BooleanField('If this notification is to be permanently pinned on the homepage.',default=False)
	def recent(self):
		'''Checks if the record is one month old? Returns true if less than one month old.'''
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False
		
class principal_desk(document):
	'''
	The articles to be uploaded under the principal's desk section.
	These are never deleted and hidden. They are always available.
	'''
	description=models.TextField('A description of the article')
	publish_date=models.DateField(default=timezone.now())
	def recent(self):
		'''Checks if the record is one month old? Returns true if less than one month old.'''
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False

	

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
	type_of_course=models.ForeignKey(course_type)

class paper(models.Model):
	'''
	Describes a paper that is taught in college.
	Each paper has an associated course.
	'''
	def __unicode__(self):
		return self.code
	code=models.CharField('The paper code',max_length=10)
	name=models.CharField('The name of paper',max_length=25)
	course=models.ForeignKey('The course associated with the paper',course)
	semester=models.IntegerField('The semester in which the paper appears',default=0)	
	
class department(models.Model):
	'''
	Describes the various departments in college.
	'''
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=35)

class society(models.Model):	
	'''
	Describes the societies in college
	'''
	def __unicode__(self):
		return self.name
	name=models.CharField('The society name',max_length=50)
	founding_date=models.DateField('The founding date of the society')
	staff_advisor=models.ForeignKey('The current staff advisor for this society',userprofile,related_name='staff_advisor')
	
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
