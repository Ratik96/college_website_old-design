from django.db import models
from django.utils import timezone
import office

class dates(models.Model):
	'''
	The important dates related to admissions
	'''
	date=models.DateField()
	activity=models.CharField(max_length=100)
	valid_upto=models.DateField()
class notice(models.Model):
	'''
	notice for admissions
	'''
	title=models.CharField(max_length=100)
	description=models.TextField()
	
	associated_file=models.FileField(upload_to='admissions/notice')
	
	publish_date=models.DateField(default=timezone.now())
	
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
	def get_hash(string):
		'''returns the hash of a string.
		length=56, sha224 implementation'''
		return hashlib.sha224(string).hexdigest()
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
	
	first_name=models.CharField(max_length=40)
	middle_name=models.CharField(max_length=40)
	last_name=models.CharField(max_length=40)
	
	picture=models.ImageField(upload_to='admissions/photos/%Y/%m/%d')
	
	email=models.EmailField()
	password=models.CharField(max_length=56)
	
	course=models.ForeignKey(office.models.course,related_name='course_applied')
	
	
	
	document_1=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_1=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_1=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	document_1=models.FileField(upload_to='admissions/documents/%Y/%m/%d',null=True,blank=True,default=None)
	
	
