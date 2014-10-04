from django.shortcuts import render
import attendance

def home(request,studentid=None):
	'''
	Homepage for attendance.
	Gives a search function to select students by course and semester if no student id is provided
	
	
	-------------------------------------
	Provides list of student_attendance objects for student if studentid has been provided.
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
			attendance.models.student_attendance.objects.filter(student=stud)
			data['student_attendance']=attendance
	return render(request,'attendance/home.html',data)			
