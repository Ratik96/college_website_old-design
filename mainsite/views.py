from django.shortcuts import render
import mainsite,office
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
	data['principal_desk']=mainsite.models.notification.objects.filter(principal=True).filter(alive=True).order_by('-publish_date','pinned')
	return render(request,'mainsite/principal_home.html',data)
def notice_view(request,noticeid):
	'''
	shows notice with given noticeid
	
	--------------------------------------------
	Provides a notice objects.=notice
	If no notice found provides
		'error'=1 for does not exist
		'error'=2 for notice not alive
	--------------------------------------------
	'''
	data={}
	try:
		notice=mainsite.models.notification.objects.get(pk=noticeid)
	except Exception as e:
		print e
		data['error']=1
	else:
		if notice.alive:
			data['notice']=notice
		else:
			print 'Notice with notice id =',noticeid,' not alive'
			data['error']=2
	return render(request,'mainsite/notice_view.html',data)		

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
def society(request):
	data={}
	return render(request,'mainsite/society.html',data)
def department(request):
	data={}
	return render(request,'mainsite/society.html',data)
def event(request):
	data={}
	return render(request,'mainsite/society.html',data)
def archive(request):
	data={}
	return render(request,'mainsite/society.html',data)
def alumni(request):
	data={}
	return render(request,'mainsite/society.html',data)
def contact(request):
	data={}
	return render(request,'mainsite/society.html',data)
