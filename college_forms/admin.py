from django.contrib import admin
from college_forms.models import *

class admission_candidate_admin(admin.ModelAdmin):
	'''
	admin for admission_candidate
	'''
	exclude=['cutoff_status']
	list_display=['thumbnail','email','stream','course','category','clear_cutoff']
	list_filter=['stream','course','category']
	search_fields=['first_name','middle_name','last_name','email']
	
admin.site.register(admission_candidate,admission_candidate_admin)
