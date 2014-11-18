from django.views.decorators.http import require_http_methods
from django.shortcuts import render,get_object_or_404
from django.http import Http404
import mainsite,office,stephens
from django.contrib.auth.models import User,Group


def home(request):
	'''
	Returns the homepage of the college website.
	Gives basic informatino and acts as an index for the site.
	
	-------------------------------------------
	Provides top 5 notification objects including pinned objects.=notification
	Provides top 5 principal desk objects.=principal_desk
	Provides Slideshow picture objects.Get url for photo by {{<object>.associated_photo.url}} in template=slideshow
	-------------------------------------------
	
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['slideshow']=mainsite.models.home_slideshow_photo.objects.all()
	data['notification']=mainsite.models.notification.objects.filter(principal=False).order_by('pinned','-publish_date')[:5]
	data['principal_desk']=mainsite.models.notification.objects.filter(principal=True).order_by('-publish_date')[:5]
	return render(request,'mainsite/home.html',data)
	
def notice_home(request):
	'''
	shows all notices which are currently active and issued.
	
	--------------------------------------------
	Provides a list of notice objects.=notifications
	--------------------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['notifications']=mainsite.models.notification.objects.filter(principal=False).order_by('-publish_date','pinned')
	return render(request,'mainsite/notice_home.html',data)
def notice_detail(request,cid):
	'''
	shows details of a notice
	'''
	data={}
	template='mainsite/notice_detail.html'
	notification=get_object_or_404(mainsite.models.notification,pk=cid)
	data['slots']=mainsite.models.Slot.objects.filter(notif=notification).order_by('order')
	data['notice']=notification
	return render(request,template,data)
	
def principal_home(request):
	'''
	shows all notices which are currently active and issued by the principal
	
	--------------------------------------------
	Provides a list of notice objects.=notification
	--------------------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['notifications']=mainsite.models.notification.objects.filter(principal=True).order_by('-publish_date','pinned')
	return render(request,'mainsite/notice_home.html',data)


def admission(request):
	'''
	Returns the homepage for admissions.
	Gives information on past,present,future admissions.
	refers to academics page for course and faculty details.
	-------------------------------------------
	Provides nothing so far.
	
	-------------------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/admission.html',data)
def academics(request):
	'''
	Returns homepage of the academics section.
	Gives information on courses,faculty etc. Everything related to academics.
	-------------------------------------------
	Provides all active members of the faculty group.list of user objects=faculty
	Provides list of courses in the college.List of course objects.=courses
	-------------------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['faculty']=office.models.faculty.objects.all()
	data['courses']=office.models.course.objects.all()
	return render(request,'mainsite/academics.html',data)
	
def society(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['societies']=office.models.society.objects.all()
	return render(request,'mainsite/society.html',data)
def society_detail(request,nick):
	'''
	returns named society
	'''
	data={}
	obj=get_object_or_404(office.models.society,nickname=nick)
	data['society']=obj
	return render(request,'mainsite/society.html',data)
def department(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['departments']=office.models.department.objects.all()
	return render(request,'mainsite/department.html',data)
def department_detail(request,nick):
	'''
	department details
	'''
	data={}
	dept=get_object_or_404(office.models.department,nickname=nick)
	data['department']=office.models.faculty.objects.filter(dept=dept)
	return render(request,'mainsite/department.html',data)
	
def archive(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/society.html',data)
def alumni(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/society.html',data)
def contact(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/contact.html',data)
def profile_detail(request,nick):
	'''
	Profile of a person
	'''
	data={}
	try:
		data['profile']=office.models.faculty.objects.get(nickname=nick)
	except:
		try:
			data['profile']=office.models.student.objects.get(nickname=nick)
		except:
			raise Http404
	if request.method=='GET':
		return render(request,'mainsite/profile.html',data)
	if request.method=='POST':
		#complete this functionality
		stephens.common_functions.contact_notification()

def course_detail(request,cid):
	'''course details'''
	data={}
	data['course']=get_object_or_404(office.models.course,pk=cid)
	data['papers']=office.models.paper.objects.filter(course=data['course'])
	return render(request,'mainsite/course.html',data)
