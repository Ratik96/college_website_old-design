from django.db import models
import office

class paper_attendence(models.Model):
	'''Class to record common characteristics for a paper's attendence records'''
	date_from=models.DateField('Date of counting first attendence.')
	date_to=models.DateField('Date of counting last attendence.')
	paper=models.ForeignKey(office.models.paper,related_name='paper')
	
	lecture=models.PositiveSmallIntegerField('Total Lecture',default=0)
	tutorial=models.PositiveSmallIntegerField('Total Tutorial',default=0)
	practical=models.PositiveSmallIntegerField('Total Practical',default=0)
		
class student_attendence(models.Model):
	'''Class to record a student's attendence in a paper'''
	student=models.ForeignKey(office.models.student,related_name='student')
	class_attendence=models.ForeignKey(paper_attendence,related_name='class_attendence')
	
	lecture=models.PositiveSmallIntegerField('Lecture Attended',default=0)
	tutorial=models.PositiveSmallIntegerField('Tutorial Attended',default=0)
	practical=models.PositiveSmallIntegerField('Practical Attended',default=0)
	
	a_lecture=models.PositiveSmallIntegerField('Lecture Adjustment(ECA etc)',default=0)
	a_tutorial=models.PositiveSmallIntegerField('Tutorial Adjustment(ECA etc)',default=0)
	a_practical=models.PositiveSmallIntegerField('Practical Adjustment(ECA etc)',default=0)

	

