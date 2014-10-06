from django.contrib import admin
from mainsite.models import *

class home_slideshow_photo_admin(admin.ModelAdmin):
	'''Admin for home_slideshow_photo'''
	fields=['name','associated_photo','alive','description']
	list_display=['thumbnail','name','associated_photo','description','alive']
	list_filter=['alive']
	search_fields=['name']
class notification_admin(admin.ModelAdmin):
	'''Admin for notification'''
	fields=['title','associated_file','alive','description','publish_date','pinned']
	list_display=['title','publish_date','recent','alive','pinned']
	list_filter=['publish_date','alive','pinned']
	search_fields=['title','description']
	
class principal_desk_admin(admin.ModelAdmin):
	'''admin for principal_desk'''
	fields=['title','associated_file','alive','description','publish_date']
	list_display=['title','publish_date','recent','alive']
	list_filter=['publish_date','alive']
	search_fields=['title','description']
	
admin.site.register(home_slideshow_photo,home_slideshow_photo_admin)
admin.site.register(notification,notification_admin)
admin.site.register(principal_desk,principal_desk_admin)
