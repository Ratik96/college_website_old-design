from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class basic_form(models.Model):
	'''
	The basics any form will have.
	'''
	user=models.ForeignKey(User,help_text='Applicant filling out form')
	submission_date=models.DateField(default=timezone.now())
	document1=models.ImageField(upload_to='forms',help_text='Supporting document 1 scanned copy',blank=True,default=None,null=True)
	document2=models.ImageField(upload_to='forms',help_text='Supporting document 2 scanned copy',blank=True,default=None,null=True)
	
	
