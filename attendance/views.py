from django.shortcuts import render
import json
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import attendance,office

def home(request):
	'''Homepage for attendance.
	Gives a search function to select students by course and semester
	-----------------GET-----------------
	Provides a list of courses=courses
	Provides a list of semesters=semesters
	----------------POST----------------
	Provides a list of students for given course and semester=students
	OR
	Provides an error variable
	
	JSON Formatted
	
	'''
	data={}
	
	if request.method=='GET':#simple http page
		data['courses']=office.models.course.objects.all()
		data['semesters']=[1,2,3,4,5,6]
		return render(request,'attendance/home.html',data)
	if request.method=='POST':#form submission
		try:
			course=office.models.course.objects.get(pk=request.POST['course'])
			semester=request.POST['semester']
		except Exception as e:
			print e
		else:
			try:
				students=office.models.student.objects.filter(course=course).filter(current_semester=semester)
				stu=[]
				for i in students:
					x={}
					x['name']=i.user.first_name.replace('_',' ').capitalize() + ' ' + i.user.last_name.capitalize()
					x['id']=i.id
					stu.append(x)
			except Exception as e:
				print e
		return HttpResponse(json.dumps(stu),content_type='application/json')
def student_id(request,studentid):
	'''
	for a student
	----------------------
	Provides attendance for student=student_attendance
	if student does not exist provides an error message
	----------------------
	'''
	data={}
	
	try:
		stud=office.models.student.objects.get(pk=studentid)
	except Exception as e:
		print e
		data['error']='Student Does not exist'
	else:
		data['student_attendance']=attendance.models.student_attendance.objects.filter(student=stud)
	return render(request,'attendance/student.html',data)
def ECA(request):
	'''A form to request ECA from the college.
	-------GET--------
	Provides a form to define the dates during which ECA is required.
	------POST--------
	Creates a new ECA object from the POST data recieved
	'''
	data={}
	template='attendance/eca.html'
	
	return render(request,template,data)
def class_attendance(request):
	'''Returns the attendance for an entire class for the last/current month to 
	be edited. Only if logged in
	'''
	data={}
	template='attendance/class.html'
	if request.user.is_authenticated():
		data['class_att']=attendance.models.paper_attendance.objects.filter(taught_by=request.user.profile)
		data['stu_att']=attendance.models.student_attendance.objects.filter(class_attendance=data['class_att'])
	else:
		data['not_authenticated']='You are not authenticated to view this page.'
	return render(request,template,data)
			
