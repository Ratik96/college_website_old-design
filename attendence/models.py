from django.db import models
import office

class attend(models.Model):
	'''The classes attended by a student'''
	lecture=models.PositiveSmallIntegerField('Lecture Field',default=0)
	tutorial=models.PositiveSmallIntegerField('Tutorial Field',default=0)
	practical=models.PositiveSmallIntegerField('Practical Field',default=0)
	
	a_lecture=models.PositiveSmallIntegerField('Lecture Adjustment',default=0)
	a_tutorial=models.PositiveSmallIntegerField('Tutorial Adjustment',default=0)
	a_practical=models.PositiveSmallIntegerField('Practical Adjustment',default=0)


class paper_attendence(models.Model):
	'''Class to record common characteristics for a paper's attendence records'''
	date_from=models.DateField('Date of counting first attendence.')
	date_to=models.DateField('Date of counting last attendence.')
	paper=models.ForeignKey(office.models.paper,related_name='paper')
	
	lecture=models.PositiveSmallIntegerField('Lecture Field',default=0)
	tutorial=models.PositiveSmallIntegerField('Tutorial Field',default=0)
	practical=models.PositiveSmallIntegerField('Practical Field',default=0)
		
class student_attendence(models.Model):
	'''Class to record a student's attendence in a paper'''
	student=models.ForeignKey(office.models.student,related_name='student')
	class_attendence=models.ForeignKey(paper_attendence,related_name='class_attendence')
	attendence=models.ForeignKey(attend,related_name='attendence')
	

	

