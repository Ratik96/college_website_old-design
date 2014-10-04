from django.shortcuts import render
import attendence

def home(request,classid=None):
	'''homepage for attendence'''
	data={}
	if classid!=None:
		try:
			course,sem,roll=map(int,classid.split('-'))
		except Exception as e:
			print e
		else:
			pass
	return render(request,'attendence/home.html',data)
