from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from attendance import views

urlpatterns = patterns(
	'',
	url(r'^(?P<studentid>\S+)?$',views.home,name='attendance_home'),
	
	
)
