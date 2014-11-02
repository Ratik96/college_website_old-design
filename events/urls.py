from django.conf.urls import patterns, include, url

from events import views

urlpatterns = patterns('',
	url(r'^$',views.home,name='event_home'),
    
)
