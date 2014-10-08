from django.shortcuts import render
from django.utils import timezone
import admission,stephens

def home(request):
	'''
	admissions homepage
	'''
	data={}
	return render(request,'admission/home.html',data)
def procedure(request):
	'''
	view defines the procedure for admission
	'''
	data={}
	return render(request,'admission/procedure.html',data)
def dates(request):
	'''
	returns important dates related to admissions
	'''
	data={}
	data['dates']=admission.models.dates.objects.filter(valid_upto__gte=timezone.now())
	return render(request,'admission/dates.html',data)
def notice(request):
	'''
	notices regarding admissions
	'''
	data={}
	data['domain_name']=stephens.settings.domain_name
	data['notices']=admission.models.notice.objects.filter(publish_date__lte=timezone.now())
	return render(request,'admission/notices.html',data)
def cutoff(request):
	'''
	cutoffs of this and previous years
	'''
	data={}
	return render(request,'admission/cutoff.html',data)
def result(request):
	'''
	results of this and previous years
	'''
	data={}
	return render(request,'admission/result.html',data)
def faq(request):
	'''
	retunrs teh frequently asked questions
	'''
	data={}
	return render(request,'admission/faq.html',data)
	
