from django.shortcuts import render
import attendance,office

def home(request,studentid=None):
	'''
	Homepage for attendance.
	Gives a search function to select students by course and semester if no student id is provided
	
	
	-------------------------------------
	Provides list of student_attendance objects for student if studentid has been provided.=student_attendance
	-------------------------------------
	
	'''
	data={}
	if studentid!=None:
		try:
			roll=int(studentid)
		except Exception as e:
			print e
		else:
			try:
				stud=office.models.student.objects.get(pk=roll)
			except Exception as e:
				print e
			else:
				data['student_attendance']=attendance.models.student_attendance.objects.filter(student=stud)
	return render(request,'attendance/home.html',data)			
