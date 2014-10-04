from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
	'',
	url(r'^',include('mainsite.urls')),
	url(r'^office/',include('office.urls')),
	url(r'^attendance/',include('attendance.urls')),
	url(r'^admin/', include(admin.site.urls)),
	#url(r'^site/',include('django.contrib.flatpages.urls')),
)
