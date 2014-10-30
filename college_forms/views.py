from django.shortcuts import render
from college_forms.models import admission_form



def home(request):
	'''
	Shows the available forms
	'''
	data={}
	data['forms']=None
	return render(request,'college_forms/home.html',data)
def admission(request):
	'''
	admission_form
	----------------------
	Provides an admission_form=form
	'''
	if request.method=='GET':
		data={}
		data['form']=admission_form()
		return render(request,'college_forms/form.html',data)
