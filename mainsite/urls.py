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
    
    url(r'^academics',views.academics,name='academics_home'),
    url(r'^admission',views.admission,name='admission_home'),
    url(r'^society',views.society,name='society_home'),
    url(r'^department',views.department,name='department_home'),
    url(r'^events',views.event,name='event_home'),
    url(r'^archive',views.archive,name='archive_home'),
    url(r'^alumni',views.alumni,name='alumni_home'),
    url(r'^contact',views.contact,name='contact_home'),
    
    url(r'^notice/$',views.notice_home,name='notice_home'),
    url(r'^principal/$',views.principal_home,name='principal_home'),
    url(r'^notice/(?P<noticeid>\d+)$',views.notice_view,name='notice_view'),
    
)
