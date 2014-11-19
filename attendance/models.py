from django.db import models
import office

class paper_attendance(models.Model):
	'''Class to record common characteristics for a paper's attendance records'''
	def __unicode__(self):
		return self.paper.__unicode__()
	date_from=models.DateField('Date of counting first attendance.')
	date_to=models.DateField('Date of counting last attendance.')
	paper=models.ForeignKey(office.models.paper,related_name='paper')
	
	lecture=models.PositiveSmallIntegerField('Total Lecture',default=0)
	tutorial=models.PositiveSmallIntegerField('Total Tutorial',default=0)
	practical=models.PositiveSmallIntegerField('Total Practical',default=0)
		
class student_attendance(models.Model):
	'''Class to record a student's attendance in a paper'''
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
