import os
import sys
import shutil
import random
import datetime
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")

from django.core.files import File
import mainsite,attendance,office,events,admission

from django.contrib.auth.models import User,Group
from django.core.management import execute_from_command_line
from django.utils import timezone

#cleanup of the existing files etc
try:
	os.remove(os.path.join(os.getcwd(),'db.sqlite3'))
except Exception as e:
	print '================================================================'
	print 'Looks like you have already removed the database.'	
	print 'here is the traceback just for completeness'
	print '================================================================'
	print e
	print '================================================================'
	print 'Moving on'
else:
	print 'Removed the existing database'
	print '================================================================'
	print 'Moving on'
	
try:
	print 'Cleaning media root'
	user=os.environ['USER']
	path='/home/'+user+'/Documents/college_site'
	shutil.rmtree(path)
except Exception as e:
	print e
else:
	print 'Done'
print '================================================================'
#cleanup complete
#create the database tables
execute_from_command_line(['manage.py','syncdb'])
#------------------------------------------------------------------------------------------------
#----------------------------------Now the setup of data starts------------------------------------------
#------------------------------------------------------------------------------------------------

function_list=[]#a list of setup function to be run
SETUP_SUPPORT_FOLDER='setup_support'#where the setup data files are located
#------------------------------------------------------------------------------------------------
def homepage_slideshow(slideshow_pic_folder='homepage'):
	'''sets up the slideshow files in the homepage'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,slideshow_pic_folder)
	files=os.listdir(filepath)
	for i in files:
		f=File(file(os.path.join(filepath,i)))
		a=mainsite.models.home_slideshow_photo()
		a.associated_photo=f
		a.name=i
		a.save()
function_list.append(homepage_slideshow)
#------------------------------------------------------------------------------------------------
def principal_desk_notices(principal_desk_folder='principal_desk'):
	'''sets up the principal desk notices'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,principal_desk_folder)
	files=os.listdir(filepath)
	for i in files:
		f=file(os.path.join(filepath,i))
		a=mainsite.models.notification()
		a.title=i.split('.')[0].replace('_',' ')
		a.principal=True
		a.associated_file=File(f)
		content=f.readlines()
		a.description=' '.join(content[:3])[:100]
		a.save()
		f.close()
function_list.append(principal_desk_notices)
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
		a=office.models.student()
		a.name=i.replace('_',' ')[:-4]
		a.picture=File(f)
		a.email=i+'@gmail.com'
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
def departments():
	'''sets up the departments'''
	department_list=[
			'Physical_education',
			'Physics',
			'Chemistry',
			'Mathematics',
			'History',
			'Philosophy',
			'English',
			'Sanskrit',
			'Hindi',
			'Administration Ofice',
			'Computer Science']
	for i in department_list:
		a=office.models.department()
		a.name=i
		a.save()
function_list.append(departments)

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
def notifications(folder='notifications'):
	'''sets up the notifications for the website'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,folder)
	files=os.listdir(filepath)
	for i in files:
		a=mainsite.models.notification()
		a.title=i.split('.')[0].replace('_',' ')
		a.description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis odio vehicula, lobortis ante hendrerit, sodales dolor. Pellentesque quis massa in tellus vulputate pretium vel id ligula. Suspendisse potenti. Donec efficitur est odio, sit amet varius eros ornare in. </p>'
		f=file(os.path.join(filepath,i))
		a.associated_file=File(f)
		a.save()
		f.close()
function_list.append(notifications)
#------------------------------------------------------------------------------------------------
def admission_important_dates():
	'''
	sets up important dates regarding admissions
	'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'admission_dates')
	f=file(filepath)
	l=f.readlines()
	f.close()
	now=timezone.now()
	next_month=datetime.datetime(now.date().year,now.date().month+1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	for i in l:
		a=admission.models.dates()
		a.date=timezone.now()
		a.activity=i
		a.valid_upto=next_month
		a.save()
function_list.append(admission_important_dates)
#------------------------------------------------------------------------------------------------
def admission_notices():
	'''
	sets up the notices regarding admissions
	'''
	pass
#------------------------------------------------------------------------------------------------
print '================================================================'
print 'SETTING UP THE WEBSITE'
print '================================================================'
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
def run_function(fn):
	'''Runs the function and acts as a wrapper'''
	print fn.func_name.replace('_',' '),
	fn()
	print '--------->Done'
	
if __name__=='__main__':
	for i in function_list:
		run_function(i)
	print '================================================================'
	print 'SETUP COMPLETE'
	print '================================================================'
