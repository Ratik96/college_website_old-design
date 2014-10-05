from django.shortcuts import render
import mainsite
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
	data['slideshow']=mainsite.models.home_slideshow_photo.objects.filter(alive=True)
	data['notification']=mainsite.models.notification.objects.filter(alive=True).order_by('-publish_date','pinned')[:5]
	data['principal_desk']=mainsite.models.principal_desk.objects.filter(alive=True).order_by('-publish_date')[:5]
	
	
	
	return render(request,'mainsite/home.html',data)
	
def admission(request):
	'''
	Returns the homepage for admissions.
	Gives information on past,present,future admissions.
	refers to academics page for course and faculty details.
	-------------------------------------------
	Provides nothing so far.
	
	-------------------------------------------
	'''
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
	grp=Group.objects.get(name='Faculty')
	data['faculty']=grp.user_set.all()
	data['courses']=office.models.course.objects.all()
	return render(request,'mainsite/academics.html',data)
