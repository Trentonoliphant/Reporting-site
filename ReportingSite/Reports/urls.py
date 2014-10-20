from django.conf.urls import patterns, url

from Reports import views

urlpatterns = patterns('',
	url(r'^$',views.ProjectsView.as_view(), name = 'projects'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/Edit/$', views.EditView.as_view(), name = 'edit'),
	url(r'^(?P<project_id>\d+)/co$', views.Submit, name = 'submit')
	)