from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory,inlineformset_factory
import json
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import attendance,office
from django.utils import timezone
from attendance import functions

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
	
@login_required
def ECA_list(request):
	data={}
	template='attendance/eca_list.html'
	#check if user is active yet
	if request.user.is_active:
		#check if user is a student
		try:
			student=office.models.student.objects.get(user=request.user)
		except Exception as e:
			print '------'
			print e
			print '------'
			data['not_authentic']='Not a student'
		else:
			data['eca_requests']=attendance.models.eca_request.objects.filter(stud=student).order_by('pk')
	else:
		data['not_authentic']='Not an active user.Contact Administration.'
	return render(request,template,data)
@login_required
def ECA_sign(request):
	"Portal for signing ECAs." 
	data={} 
	template='attendance/eca_sign.html' 
	factory=modelformset_factory(attendance.models.eca_request,extra=0,exclude=['approved'],can_delete=False)
	if request.method=='GET':
		user=request.user
		unsigned=functions.get_unsigned_eca_requests(user)
		if unsigned!=None:
			data['formset']=factory(queryset=unsigned)
			data['status']='You have unsigned ECA requests.'
		return render(request,template,data)
	if request.method=='POST':
		user=request.user
		unsigned=functions.get_unsigned_eca_requests(user)
		signed=factory(request.POST,queryset=unsigned)
		if signed.is_valid():
			fac=office.models.faculty.objects.get(user=user)
			signed.save()
			data['status']='Successfully signed ECA requests'
			data['formset']=factory(queryset=unsigned)
		else:
			data['formset']=signed
			data['status']='Your entries did not validate. Please resubmit'
		return render(request,template,data)
	data['status']='Something went wrong. If problem persists contact Website Admin'
	return render(request,template,data)
	
@login_required
def ECA_approve(request):
	'''Portal for ECA approval'''
	data={}
	template='attendance/eca_approve.html'
	factory=modelformset_factory(attendance.models.eca_request,extra=0,exclude=['approved'],can_delete=False)
	if request.method=='GET':
		user=request.user
		unsigned=functions.get_unapproved_eca_requests(user)
		if unsigned!=None:
			data['formset']=factory(queryset=unsigned)
			data['status']='You have unsigned ECA requests.'
		return render(request,template,data)
	if request.method=='POST':
		user=request.user
		unsigned=functions.get_unapproved_eca_requests(user)
		signed=factory(request.POST,queryset=unsigned)
		if signed.is_valid():
			fac=office.models.faculty.objects.get(user=user)
			signed.save()
			data['status']='Successfully signed ECA requests'
			data['formset']=factory(queryset=unsigned)
		else:
			data['formset']=signed
			data['status']='Your entries did not validate. Please resubmit'
		return render(request,template,data)
	data['status']='Something went wrong. If problem persists contact Website Admin'
	return render(request,template,data)
@login_required
def ECA_new(request):
	'''A form to request ECA from the college.
	-------GET--------
	Provides a form to define the dates during which ECA is required.
	------POST--------
	Creates a new ECA object from the POST data recieved
	'''
	data={}
	template='attendance/eca_new.html'
	#if user is active or not
	if request.user.is_active:
		#check if the user is a student and registered
		try:
			student=office.models.student.objects.get(user=request.user)
		except Exception as e:
			print '-----------'
			print e
			print '-----------'
			data['not_authentic']='You must be a student to submit ECA'
			#if not then return error
			return render(request,template,data)
		else:
			#make the dates formset
			formset=inlineformset_factory(attendance.models.eca_request,attendance.models.eca_date,extra=10,can_delete=False)
			if request.method=='GET':
				#return an empty form
				data['form']=formset(initial=[{'start':timezone.now()}])
				data['detail']=attendance.models.eca_request_form()
				data['status']='New ECA submission'
			if request.method=='POST':
				#print 'detail_form-------debug'
				#get the details for the eca request
				detail_form=attendance.models.eca_request_form(request.POST)
				if detail_form.is_valid():
					eca_details=detail_form.save(commit=False)
					eca_details.stud=office.models.student.objects.get(user=request.user)
					eca_details.save()
				else:
					#if not valid return the errors found
					data['detail']=detail_form
					return render(request,template,data)
				#print 'Detail  form done---------debug'
				dates=formset(request.POST,instance=eca_details)
				if dates.is_valid():
					dates.save()
					#print 'dates done------debug'
					data['status']='Successfully submitted ECA'
					data['form']=formset(initial=[{'start':timezone.now()}])
					data['detail']=attendance.models.eca_request_form()
					#return completed status
				else:
					data['detail']=detail_form
					data['form']=dates
	else:
		data['not_authentic']='Not logged in'
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

def ECA_home(request):
	'''Returns the links of various ECA functinoalities based on student/faculty/anoonymous users'''
	data={}
	template='attendance/eca_home.html'
	user=request.user
	if user.is_authenticated():
		try:
			stu=office.models.student.objects.get(user=user)
		except:
			data['faculty']=True
		else:
			data['student']=True
	return render(request,template,data)
