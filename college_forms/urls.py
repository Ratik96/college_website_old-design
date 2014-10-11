from django.conf.urls import patterns, include, url
from college_forms import views

urlpatterns = patterns(
	'',
	url('^admission$',views.admission,name='admission_form'),
	
	)
