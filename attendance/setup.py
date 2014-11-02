import os
import sys
import shutil
import random
import datetime
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")

from django.core.files import File

from django.contrib.auth.models import User,Group
from django.core.management import execute_from_command_line
from django.utils import timezone

def clean_to_string(string):
	'''
	removes non ascii characters
	'''
	allowed='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'#alphabets
	allowed+=allowed.lower()#lowercase
	allowed+='!@#$%^&*()_+=-.,: '
	allowed+="'"
	allowed+='\n'
	new_str=''
	for i in string:
		if i in allowed:
			new_str+=i
	return new_str
import mainsite,attendance,office,events,admission,college_forms
function_list=[]
SETUP_SUPPORT_FOLDER='setup_support'

#------------------------------------------------------------------------------------------------
def student_attendance():
	'''sets up the attendance for the dummy students'''
	course=office.models.course.objects.first()
	papers=office.models.paper.objects.filter(course=course).order_by('-pk')[:4]
	students=office.models.student.objects.all()
	for p in papers:
			pap_attd=attendance.models.paper_attendance()
			pap_attd.date_from=timezone.now()
			pap_attd.date_to=timezone.now()
			pap_attd.paper=p
			pap_attd.lecture=random.choice(range(40,50))
			pap_attd.practical=random.choice(range(20,35))
			pap_attd.tutorial=random.choice(range(7,12))
			pap_attd.save()
	for stud in students:
		pap_attds=attendance.models.paper_attendance.objects.all()
		for p in pap_attds:
			a=attendance.models.student_attendance()
			a.student=stud
			a.class_attendance=p
			a.lecture=random.choice(range(int(p.lecture*0.1),(p.lecture)))
			a.practical=random.choice(range(int(p.practical*0.1),(p.practical)))
			a.tutorial=random.choice(range(int(p.tutorial*0.1),(p.tutorial)))
			a.save()
function_list.append(student_attendance)
#------------------------------------------------------------------------------------------------
def run_function(fn):
	'''Runs the function and acts as a wrapper'''
	print fn.func_name.replace('_',' ').capitalize(),
	fn()
	print '--------->Done'
	
def run_setup():
	print '================================================================'
	for i in function_list:
		run_function(i)	
	print 'ATTENDANCE SETUP COMPLETE'
	print '================================================================'
	
