import os
import sys
import shutil
import random
import datetime
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")

from django.core.files import File
import mainsite,attendance,office,events,admission,college_forms

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
execute_from_command_line(['manage.py','syncdb','--noinput'])
sup=User()
sup.is_staff=True
sup.is_superuser=True
sup.set_password('asd')
sup.username='ghost'
sup.save()
#------------------------------------------------------------------------------------------------
#----------------------------------Now the setup of data starts------------------------------------------
#------------------------------------------------------------------------------------------------
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
	next_month=datetime.datetime(now.date().year,now.date().month+1,20,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
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
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'admission_notices')
	files_available=os.listdir(filepath)
	for i in files_available:
		a=admission.models.notice()
		a.title=i
		a.description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis odio vehicula, lobortis ante hendrerit, sodales dolor. Pellentesque quis massa in tellus vulputate pretium vel id ligula. Suspendisse potenti. Donec efficitur est odio, sit amet varius eros ornare in. </p>'
		a.publish_date=timezone.now()
		f=file(os.path.join(filepath,i))
		a.associated_file=File(f)
		a.save()
		f.close()
function_list.append(admission_notices)
#------------------------------------------------------------------------------------------------
def admission_categories():
	'''
	sets up the admission categories
	'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'admission_cutoff')
	f=file(os.path.join(filepath,'category'))
	l=f.readlines()
	f.close()
	for i in l:
		a=admission.models.category()
		a.name,a.code=i.split(',')
		a.save()
function_list.append(admission_categories)		
#------------------------------------------------------------------------------------------------
def admission_cutoff_and_courses():
	'''
	sets up the courses and the cutoffs in the college
	'''
	for c in office.models.course.objects.all():
		cs=admission.models.cutoff_subject()
		cs.valid_upto=timezone.now()
		cs.course=c
		cs.save()
		for i in admission.models.category.objects.all():
			a=admission.models.category_cutoff()
			a.category=i
			a.cutoff_subject=cs
			x=random.random()
			a.science=round(random.choice([70,60,80])+(x*19),2)
			x=random.random()
			a.humanities=round(random.choice([70,60,80])+(x*19),2)
			x=random.random()
			a.commerce=round(random.choice([70,60,80])+(x*19),2)
			a.save()
	
function_list.append(admission_cutoff_and_courses)
#------------------------------------------------------------------------------------------------
def admission_candidates():
	'''
	sets up the results in the interviews and such
	'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'admission_candidates')
	files=os.listdir(filepath)
	courses_available=office.models.course.objects.all()
	category_available=admission.models.category.objects.all()
	for i in files:
		ac=college_forms.models.admission_candidate()
		temp_name=i.strip('.jpg').split('_')
		ac.first_name=temp_name[0]
		ac.last_name=temp_name[-1]
		try:
			ac.middle_name=temp_name[1] if temp_name[1]!=temp_name[-1] else ''
		except:
			pass
		f=file(os.path.join(filepath,i))
		ac.picture=File(f)
		ac.email=i+'@gmail.com'
		ac.password='arjoonn'
		ac.stream=random.choice([1,2,3])
		ac.course=random.choice(courses_available)
		ac.category=random.choice(category_available)
		ac.bfs=round((80+(random.random()*20)),2)
		ac.save()
		f.close()
function_list.append(admission_candidates)
		
			
			
#------------------------------------------------------------------------------------------------
def FAQ():
	'''
	sets up the faq for the website
	'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'admission_FAQ')
	q_file=file(os.path.join(filepath,'question'))
	lines=q_file.readlines()
	q_file.close()
	q_a=[]
	temp=[]
	for i,k in enumerate(lines):
		if i%2==0:
			temp.append(k)
		if i%2!=0:
			temp.append(k)
			q_a.append(temp)
			temp=[]
	for k,i in enumerate(q_a):
		a=admission.models.q_a()
		a.question=i[0]
		a.answer=i[1]
		a.rank=k
		a.save()
function_list.append(FAQ)
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
def locations():
	'''
	locations in college'''
	filepath=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'locations')
	f=file(filepath)
	loc=f.readlines()
	f.close()
	for i in loc:
		l=events.models.Location()
		l.name=l.strip()[:40]
		l.save()
function_list.append(locations)
#------------------------------------------------------------------------------------------------
def events_in_college():
	ev_path=os.path.join(os.getcwd(),SETUP_SUPPORT_FOLDER,'events')
	
function_list.append(events_in_college)
#------------------------------------------------------------------------------------------------
print '================================================================'
print 'SETTING UP THE WEBSITE'
print '================================================================'
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
def run_function(fn):
	'''Runs the function and acts as a wrapper'''
	print fn.func_name.replace('_',' ').capitalize(),
	fn()
	print '--------->Done'
	
if __name__=='__main__':
	for i in function_list:
		run_function(i)
	print '================================================================'
	print 'SETUP COMPLETE'
	print '================================================================'
