from django.contrib import admin

from office.models import *


class course_inline(admin.TabularInline):
	'''inline addition for course_type'''
	model=course
	
class course_type_admin(admin.ModelAdmin):
	'''admin for course'''
	inlines=[course_inline]
class profile_admin(admin.ModelAdmin):
	'''admin for profile'''
	list_display=['thumbnail','user','joining_date']
	list_filter=['joining_date','dept']
	search_fields=['user']
	
class student_admin(admin.ModelAdmin):
	'''admin for student'''
	list_display=['thumbnail','name','email']
	list_filter=['course','admission_date']
	search_fields=['name','email']
admin.site.register(course)
admin.site.register(course_type,course_type_admin)
admin.site.register(paper)
admin.site.register(department)
admin.site.register(society)
admin.site.register(student,student_admin)
admin.site.register(profile,profile_admin)
