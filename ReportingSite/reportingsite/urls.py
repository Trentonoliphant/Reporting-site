from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reportingsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^',include('Reports.urls', namespace='reports')),
    url(r'^admin/', include(admin.site.urls)),
)
