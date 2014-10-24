from django.conf.urls import patterns, url

from Reports import views

urlpatterns = patterns('',
	url(r'^$',views.HomeView.as_view(), name = 'home'),
	url(r'^submit$', views.Submit_month, name = 'submit'),
	url(r'^201\d-(0[1-9])|(1[0-2])/$', views.OverviewView.as_view(), name='Overview'),
	#url(r'^(?P<pk>\d+)/Edit/$', views.EditView.as_view(), name = 'edit'),
	#url(r'^(?P<project_id>\d+)/co$', views.Submit, name = 'submit')
	)