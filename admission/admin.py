from django.contrib import admin

from admission.models import *
class dates_admin(admin.ModelAdmin):
	list_display=['activity','date','valid_upto']
	list_filter=['date','valid_upto']
	search_fields=['activity']
class notice_admin(admin.ModelAdmin):
	list_display=['title','publish_date']
	list_filter=['publish_date']
	search_fields=['title','description']
	
class category_cutoff_inline(admin.TabularInline):
	'''
	inline model for category cutoff
	'''
	model=category_cutoff
class cutoff_subject_admin(admin.ModelAdmin):
	'''
	admin for cutoffs
	'''
	inlines=[category_cutoff_inline]
	
class admission_candidate_admin(admin.ModelAdmin):
	'''
	admin for admission_candidate
	'''
	list_display=['email','stream','course','category','clear_cutoff']
	list_filter=['stream','course','category']
	search_fields=['first_name','middle_name','last_name','email']
	
admin.site.register(admission_candidate,admission_candidate_admin)
admin.site.register(cutoff_subject,cutoff_subject_admin)
admin.site.register(dates,dates_admin)
admin.site.register(notice,notice_admin)
