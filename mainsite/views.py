from django.shortcuts import render
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
	data['slideshow']=mainsite.models.home_slideshow_photo.objects.filter(alive=True)
	data['notification']=mainsite.models.notification.objects.filter(principal=False).filter(alive=True).order_by('pinned','-publish_date')[:5]
	data['principal_desk']=mainsite.models.notification.objects.filter(principal=True).filter(alive=True).order_by('-publish_date')[:5]
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
	data['notifications']=mainsite.models.notification.objects.filter(principal=False).filter(alive=True).order_by('-publish_date','pinned')
	return render(request,'mainsite/notice_home.html',data)
def principal_home(request):
	'''
	shows all notices which are currently active and issued by the principal
	
	--------------------------------------------
	Provides a list of notice objects.=notification
	--------------------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['principal_desk']=mainsite.models.notification.objects.filter(principal=True).filter(alive=True).order_by('-publish_date','pinned')
	return render(request,'mainsite/principal_home.html',data)


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
	grp=Group.objects.get(name='Faculty')
	data['faculty']=grp.user_set.all()
	data['courses']=office.models.course.objects.all()
	return render(request,'mainsite/academics.html',data)
def society(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/society.html',data)
def department(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/society.html',data)
def event(request):
	data={}
	data['domain_name']=stephens.settings.domain_name
	return render(request,'mainsite/society.html',data)
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
	return render(request,'mainsite/society.html',data)
