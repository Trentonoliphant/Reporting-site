from django.conf.urls import patterns, url

from Reports import views

urlpatterns = patterns('',
	url(r'^$',views.MonthView.as_view(), name = 'month'),
	url(r'^\d{4}-\d{2}/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>\d+)/Edit/$', views.EditView.as_view(), name = 'edit'),
	#url(r'^(?P<project_id>\d+)/co$', views.Submit, name = 'submit')
	)