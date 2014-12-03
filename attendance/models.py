import office
import random
from django.db import models
from django.utils import timezone
from django.forms import ModelForm


class paper_attendance(models.Model):
	'''Class to record common characteristics for a paper's attendance records.
	It is common for all student studying the paper.
	Date_from=starting attendance date
	Date_to=ending attendance date
	paper=paper for which attendance will be recorded
	
	The lecture,tutorial,practical totals for this paper
	'''
	def __unicode__(self):
		return self.paper.__unicode__()
	date_from=models.DateField('Date of counting first attendance.')
	date_to=models.DateField('Date of counting last attendance.')
	paper=models.ForeignKey(office.models.paper,related_name='paper')
	
	taught_by=models.ForeignKey(office.models.faculty,related_name='taught_by',default=None,blank=True,null=True)
	
	lecture=models.PositiveSmallIntegerField('Total Lecture',default=0)
	tutorial=models.PositiveSmallIntegerField('Total Tutorial',default=0)
	practical=models.PositiveSmallIntegerField('Total Practical',default=0)
		
class student_attendance(models.Model):
	'''Class to record a student's attendance in a paper.
	Student attendance in a paper.
	Relates to a class attendance which holds the total attendance.
	The classes attended and the adjustments for the classes.
	'''
	def __unicode__(self):
		return self.student.__unicode__()+'-'+self.class_attendance.paper.__unicode__()
	student=models.ForeignKey(office.models.student,related_name='student')
	class_attendance=models.ForeignKey(paper_attendance,related_name='class_attendance')
	
	lecture=models.PositiveSmallIntegerField('Lecture Attended',default=0)
	tutorial=models.PositiveSmallIntegerField('Tutorial Attended',default=0)
	practical=models.PositiveSmallIntegerField('Practical Attended',default=0)
	
	a_lecture=models.PositiveSmallIntegerField('Lecture Adjustment(ECA etc)',default=0)
	a_tutorial=models.PositiveSmallIntegerField('Tutorial Adjustment(ECA etc)',default=0)
	a_practical=models.PositiveSmallIntegerField('Practical Adjustment(ECA etc)',default=0)
class eca_request(models.Model):
	'''Class to store an ECA request'''
	stud=models.ForeignKey(office.models.student,related_name='stud')
	approved=models.BooleanField(default=False)
	description=models.TextField(help_text='Nature of activity requiring absence from class.')
	soc=models.ForeignKey(office.models.deptsoc,related_name='society',help_text='Department/Society under which activity was done.')
	#add signed also
class eca_date(models.Model):
	'''Class to store ECA date'''
	related_eca_request=models.ForeignKey(eca_request)
	start=models.DateTimeField()
	end=models.DateTimeField()
class eca_request_form(ModelForm):
	class Meta:
		model=eca_request
		exclude=['approved','stud']
class eca_date_form(ModelForm):
	class Meta:
		model=eca_date
		fields=['start','end']
class attendance_log(models.Model):
	'''A class to keep track of the activities in the attendance models'''
	stamp=models.DateTimeField(default=timezone.now())
	text=models.TextField()
