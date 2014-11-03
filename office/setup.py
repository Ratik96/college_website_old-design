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
import mainsite,attendance,office,events,admission,college_forms

def clean_to_string(string):
	'''
	removes non ascii characters
	'''
	allowed='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'#alphabets
	allowed+=allowed.lower()#lowercase
	allowed+='''!@#$%^&*()'_+=-.,: '''#Special characters
	allowed+='\n\t'#newline etc
	new_str=''
	for i in string:
		if i in allowed:
			new_str+=i
	return new_str
function_list=[]
SETUP_SUPPORT_FOLDER='setup_support'
#------------------------------------------------------------------------------------------------
def course_type():
	'''sets up the course types'''
	name_list=['Undergraduate','Postgraduate','Vocational','Language']
	for i in name_list:
		a=office.models.course_type()
		a.name=i
		a.save()
function_list.append(course_type)
#------------------------------------------------------------------------------------------------
def courses():
	'''sets up the courses in undergraduate'''
	names=['B.Sc. Physical Science','B.Sc. Chemistry','B.Sc. Mathematics','B.Sc. Physics','B.A. History','B.A. Philosophy','B.A. Programme']
	ug_course_type=office.models.course_type.objects.first()
	for i in names:
		a=office.models.course()
		a.name=i
		a.course_type=ug_course_type
		a.save()
function_list.append(courses)
#------------------------------------------------------------------------------------------------
def students(student_photo_folder='student_photos'):
	'''sets up dummy students'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,student_photo_folder)
	files=os.listdir(filepath)
	for i in files:
		f=file(os.path.join(filepath,i))
		u=User()
		u.username=i[:-4]
		u.first_name=i[:-4]
		u.email=i+'@gmail.com'
		u.set_password('asd')
		u.save()
		
		a=office.models.student()
		a.user=u
		a.picture=File(f)
		a.course=office.models.course.objects.first()
		a.save()
		
		f.close()
function_list.append(students)
#------------------------------------------------------------------------------------------------
def groups():
	'''sets up the groups'''
	groupnames=[
		{'n':'Principal',
		'p':None},
		{'n':'Bursar',
		'p':None},
		{'n':'Dean(Residence)',
		'p':None},
		{'n':'Dean(Academic Affairs)',
		'p':None},
		{'n':'Chaplain',
		'p':None},
		{'n':'Public Information Officer',
		'p':None},
		{'n':'Special Assignments',
		'p':None},
		{'n':'Administration',
		'p':None},
		{'n':'Staff Advisor',
		'p':None},
		{'n':'Faculty',
		'p':None},
		{'n':'Students',
		'p':None}]
	for i in groupnames:
		a=Group()
		a.name=i['n']
		a.save()
function_list.append(groups)
#------------------------------------------------------------------------------------------------
def university_papers():
	'''sets up the papers'''
	paper_list=['MAPT-101','PHPT-101','CSPT-101','CHPT-101',
		'MAPT-202','PHPT-202','CSPT-202','CHPT-202',
		'MAPT-303','PHPT-303','CSPT-303','CHPT-303',
		'MAPT-404','PHPT-404','CSPT-404','CHPT-404',
		'MAPT-505','PHPT-505','CSPT-505','CHPT-505',
		'MAPT-606','PHPT-606','CSPT-606','CHPT-606',
		]
	bsc_course=office.models.course.objects.first()
	for i in paper_list:
		a=office.models.paper()
		a.code=i
		a.name=i
		a.course=bsc_course
		a.semester=int(i[-1])
		a.save()
function_list.append(university_papers)

#------------------------------------------------------------------------------------------------
def faculty():
	'''
	adds faculty. and departments'''
	
	prof_path=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'profile')
	default_picture=File(file(os.path.join(prof_path,'default.jpg')))#default profile picture
	depts=os.listdir(os.path.join(prof_path,'profiles'))#list of departments
	for dept in depts:
		#create department
		department=office.models.department()
		department.name=dept.strip().replace('_',' ')
		department.nickname=clean_to_string(dept.strip().replace('_','').replace(' ','').replace('/','').lower())[:5]
		department.save()
		#list profiles in the department
		profiles=os.listdir(os.path.join(prof_path,'profiles',dept))
		for prof in profiles:
			#create profiles
			f=file(os.path.join(prof_path,'profiles',dept,prof))
			det=f.readlines()
			f.close()
			user=User()
			user.username=prof.strip().replace(' ','').replace('.','').lower()[:-3]
			user.first_name=clean_to_string(prof.strip()[:-4])#account for the extra dot
			user.set_password('asd')
			user.save()
			#create profile
			profile=office.models.faculty()
			profile.user=user
			profile.nickname=prof.strip().replace(' ','').replace('.','').lower()[:-3]
			profile.title=''
			profile.picture=default_picture
			profile.dept=department
			profile.qualification=clean_to_string(det[2].strip())
			profile.save()
function_list.append(faculty)
#------------------------------------------------------------------------------------------------

def societies():
	'''
	adds societies for the college
	'''
	soc_path=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'Societies')
	socs=os.listdir(soc_path)
	for i in socs:
		cur_path=os.path.join(soc_path,i)
		accepted="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'"
		accepted+='":,.!@#$%^&*()_+=- '
		accepted+='\n'
		files=os.listdir(cur_path)
		for k in files:
			if ('D' or 'd') in k:
				f_d=file(os.path.join(cur_path,k))
			else:
				f_nick=file(os.path.join(cur_path,k))
		det=f_d.readlines()
		det_new=[]
		for k in det:
			temp=''
			for j in k:
				if j in accepted:
					temp+=j
			temp+='\n'
			det_new.append(temp)
		det=det_new
		try:
			nicks=f_nick.readlines()[0].strip()
		except :
			nicks=i.strip().replace(' ','')[:10].strip()
		f_d.close()
		f_nick.close()
		#accepted the nicknames and details
		soc=office.models.society()
		soc.name=i.strip()
		soc.nickname=nicks
		soc.founding_date=timezone.now()
		soc.staff_advisor=office.models.faculty.objects.first()
		soc.description=unicode(''.join(det_new))
		soc.save()
function_list.append(societies)
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
	print 'OFFICE SETUP COMPLETE'
	print '================================================================'
	