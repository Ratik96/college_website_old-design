from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
import mainsite

class Notifications_feed(Feed):
	'''
	Feed class to implement the college Notifications class
	'''
	title="Notifications from college"
	link="/sitenews/"
	description="Updates on changes and additions to notifications by the college."

	def items(self):
		return mainsite.models.notification.objects.filter(principal=False).order_by('-publish_date')[:10]
	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return item.description

	# item_link is only needed if NewsItem has no get_absolute_url method.
	def item_link(self,item):
		return reverse('notice_view',args=[item.pk])
class Principal_feed(Feed):
	'''
	Feed class to implement a RSS feed for principal's desk
	'''
	title="Notifications from Principal's Desk"
	link="/sitenews/"
	description="Updates on changes and additions to the Principal's Desk."

	def items(self):
		return mainsite.models.notification.objects.filter(principal=True).order_by('-publish_date')[:10]
	def item_title(self,item):
		return item.title

	def item_description(self,item):
		return item.description

	# item_link is only needed if NewsItem has no get_absolute_url method.
	def item_link(self,item):
		return reverse('notice_view',args=[item.pk])
