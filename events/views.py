from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from events import models

def home(request):
	'''
	The homepage for events. Must display a calender of events.
	and navigation for the rest of the app
	'''
	data={}
	template='events/home.html'
	ev=models.Event.objects.filter(start__gte=timezone.now())#events in future
	ev.order_by('start','start__weekday')
	data['events']=ev
	return render(request,template,data)
