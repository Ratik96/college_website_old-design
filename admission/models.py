from django.db import models
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

class results(models.Model):
	'''
	students selected in to courses
	'''
	pass
	
class admission_candidate(models.Model):
	'''
	model to represent an admission candidate
	-----------------------------------------
	Things to be supplied by candidate
	1. name
	2. valid email id
	3. photograph
	4. marksheets
	5. payment challans
	'''
	def __unicode__(self):
		return str(self.first_name)+str(self.middle_name)+str(self.last_name)
	def set_password(self,string):
		'''
		sets the password value  to the hash of the given string
		'''
		self.password=get_hash(string)
	def check_password(self,string):
		'''
		checks if string is same as the password by comparing hashes
		'''
		current=self.password
		entered=get_hash(string)
		if current==entered:
			return True
		return False
	def clear_cutoff(self):
		'''
		checks if candidate clears cutoff
		'''
		old_value=self.cutoff_status
		new_value=old_value
		if len(category_cutoff.objects.all())==0:
			new_value=False#ie no cutoffs have been declared
			
		cutoff=category_cutoff.objects.filter(cutoff_subject__course=self.course).filter(category=self.category).filter(cutoff_subject__valid_upto__lte=timezone.now())[0]
		
		if self.stream==1:#from science
			if self.bfs>=cutoff.science:
				new_value=True
			else:
				new_value=False
		if self.stream==2:#from commerce
			if self.bfs>=cutoff.commerce:
				new_value=True
			else:
				new_value=False
		if self.stream==3:#from humanities
			if self.bfs>=cutoff.humanities:
				new_value=True
			else:
				new_value=False
		if new_value==old_value:
			return new_value
		else:
			self.cutoff_status=new_value
			self.save()
			return new_value
			
		
	clear_cutoff.boolean=True
	clear_cutoff.short_description='Has cleared course cutoff?'
	clear_cutoff.admin_order_field='cutoff_status'
	
	
	first_name=models.CharField(max_length=40)
	middle_name=models.CharField(max_length=40,blank=True)
	last_name=models.CharField(max_length=40,blank=True)
	picture=models.ImageField(upload_to='admissions/photos/%Y/%m/%d')
	email=models.EmailField()
	password=models.CharField(max_length=56)
	
	STREAM_CHOICES=[
			(1,'Sciences'),
			(2,'Commerce'),
			(3,'Humanities')
			]
			
	stream=models.SmallIntegerField('Stream applicable to you',choices=STREAM_CHOICES)
	course=models.ForeignKey(office.models.course,related_name='course_applied',help_text='Course you want to apply for')
	category=models.ForeignKey(category,related_name='category_applied',help_text='Category applicable to you')
	bfs=models.FloatField("Best Four Subject's Marks")
	cutoff_status=models.BooleanField(default=False)

	
	document_1=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_2=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_3=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_4=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	
	
