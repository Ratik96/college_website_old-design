from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from mainsite import views,feeds

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stephens.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',views.home,name='site_home'),
    url(r'^notification_rss',feeds.Notifications_feed(),name='notification_feed'),
    url(r'^principal_rss',feeds.Principal_feed(),name='principal_feed'),
)