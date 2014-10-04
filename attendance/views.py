from django.shortcuts import render
import attendence

def home(request,studentid=None):
	'''
	Homepage for attendence.
	Gives a search function to select students by course and semester if no student id is provided
	
	
	-------------------------------------
	Provides list of student_attendence objects for student if studentid has been provided.
	-------------------------------------
	
	'''
	data={}
	if studentid!=None:
		try:
			roll=int(studentid)
		except Exception as e:
			print e
		else:
			stud=office.models.otudent.objects.get(pk=roll)
			attendence.models.student_attendence.objects.filter(student=stud)
			data['student_attendance']=attendence
	return render(request,'attendance/home.html',data)			
