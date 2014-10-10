from django.shortcuts import render
from django.utils import timezone
import admission,stephens

def home(request):
	'''
	admissions homepage.
	Try to implement as a flatpage...
	'''
	data={}
	return render(request,'admission/home.html',data)
def procedure(request):
	'''
	view defines the procedure for admission
	To be flatpaged....
	'''
	data={}
	return render(request,'admission/procedure.html',data)
def dates(request):
	'''
	returns important dates related to admissions
	-------------------------------
	Provides a list of dates object=dates
	-------------------------------
	'''
	data={}
	data['dates']=admission.models.dates.objects.filter(valid_upto__gte=timezone.now())
	return render(request,'admission/dates.html',data)
def notice(request):
	'''
	notices regarding admissions
	----------------------------------
	Provides a list of notices=notices
	----------------------------------
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['notices']=admission.models.notice.objects.filter(publish_date__lte=timezone.now())
	return render(request,'admission/notices.html',data)
def cutoff(request):
	'''
	cutoffs of this year
	-------------------------------------
	Provides a list of category cutoffs=cutoffs
	Provides a list of subjects and their cutoff validation dates=courses
	-------------------------------------
	'''
	data={}
	data['courses']=admission.models.cutoff_subject.objects.all()
	data['cutoffs']=admission.models.category_cutoff.objects.filter(cutoff_subject__valid_upto__gte=timezone.now()).order_by('cutoff_subject','category')
	return render(request,'admission/cutoff.html',data)
	
def result(request):
	'''
	results of this and previous years
	-------------------------------------
	Provides a list of admitted candidates=admitted
	-------------------------------------
	'''
	data={}
	data['admitted']=admission.models.admission_candidate.objects.filter(cutoff_status=True).filter(admitted=True)
	print data['admitted']
	return render(request,'admission/result.html',data)
	
def faq(request):
	'''
	retunrs the frequently asked questions with answers.
	User can ask a new question.
	-------------------------------------
	Provides a list of q_a objects=q_a
	-------------------------------------
	'''
	data={}
	data['q_a']=admission.models.q_a.objects.order_by('rank')
	return render(request,'admission/faq.html',data)
def admission_form(request):
	'''
	Displays the admission form on login.
	Register a new user if needed.
	'''
	pass
