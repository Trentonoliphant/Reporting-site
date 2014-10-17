from django.conf.urls import patterns, url

from Reports import views

urlpatterns = patterns('',
	url(r'^$',views.ReportView.as_view(), name = 'report'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	)