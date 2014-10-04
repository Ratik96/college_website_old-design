from django.contrib import admin
import attendance


class student_attendance_inline(admin.TabularInline):
	'''Inline addition for student_attendance'''
	model=attendance.models.student_attendance
	extra=20
	
class paper_attendance_admin(admin.ModelAdmin):
	'''Paper attendance admin'''
	
	inlines=[student_attendance_inline]
	list_display=['paper','date_from','date_to']
	list_filter=['date_from','date_to']
	search_fields=['paper']


admin.site.register(attendance.models.student_attendance)
admin.site.register(attendance.models.paper_attendance,paper_attendance_admin)
