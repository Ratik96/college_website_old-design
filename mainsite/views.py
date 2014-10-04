from django.shortcuts import render
import mainsite


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
	
