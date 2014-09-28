from django.shortcuts import render
import mainsite


def home(request):
	data={}
	data['slideshow']=mainsite.models.home_slideshow_photo.objects.filter(alive=True)
	data['notification']=mainsite.models.notification.objects.filter(alive=True).order_by('pinned','-publish_date')[:5]
	data['principal_desk']=mainsite.models.principal_desk.objects.filter(alive=True).order_by('-publish_date')[:5]
	#added the slideshow pictures and the notifications and principal's desk items
	
	
	
	return render(request,'mainsite/home.html',data)
	
