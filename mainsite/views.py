from django.shortcuts import render
import mainsite
def home(request):
	data={}
	pics=mainsite.models.home_slideshow_photo.objects.filter(alive=True)
	data['slideshow']=pics
	return render(request,'mainsite/home.html',data)
	
