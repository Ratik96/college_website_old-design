from django.contrib import admin
from mainsite.models import *

class home_slideshow_photo_admin(admin.ModelAdmin):
	'''Admin for home_slideshow_photo'''
	fields=['name','associated_photo','description']
	list_display=['thumbnail','name','associated_photo','description']
	search_fields=['name','description']
class notification_admin(admin.ModelAdmin):
	'''Admin for notification'''
	fields=['title','associated_file','alive','description','publish_date','pinned']
	list_display=['title','publish_date','recent','alive','pinned']
	list_filter=['publish_date','alive','pinned']
	search_fields=['title','description']
	

admin.site.register(home_slideshow_photo,home_slideshow_photo_admin)
admin.site.register(notification,notification_admin)

