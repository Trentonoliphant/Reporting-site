from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import calendar


from Reports.models import Employee, Project, Hours_report

class ProjectsView(generic.ListView):
	template_name = 'Reports/projects.html'
	context_object_name = 'projects_list'

	def get_queryset(self):
		return Project.objects.all()



class OverviewView(generic.ListView):
	
	template_name = 'Reports/Overview.html'

	context_object_name = 'Project'

	def get_context_data(self, **kwargs):
		ctx = super(OverviewView, self).get_context_data(**kwargs)
		ctx['Employee'] = Employee.objects.all()
		ctx['Hours_report'] = Hours_report.objects.all().order_by('Project')
		return ctx

	def get_queryset(self):
		return Project.objects.all()

	#def get_queryset(self):
	#	weeks = {'4':'2014-10-01','3':'2014-10-14'}

	#	week = weeks[self.kwargs['pk']]
	#	return .objects.filter(Week_of=week).order_by('Employee')



class HomeView(generic.ListView):
	template_name = 'Reports/home.html'
	months = [calendar.month_name[i] for i in range(1, 13)]
	context_object_name ='months'
	years = [i for i in range(2012,2016)]
	
	def get_queryset(self):
		return self.months

	def get_context_data(self, **kwargs):
		ctx = super(HomeView, self).get_context_data(**kwargs)
		ctx['years'] = self.years
		return ctx



def Submit_month(request):
	p = request.POST['month']
	return HttpResponseRedirect('reports:Overview')



class EditView(generic.DetailView):
	model = Project

	template_name = 'Reports/edit.html'
	context_object_name = 'project'

	def get_context_data(self, **kwargs):
		ctx = super(EditView, self).get_context_data(**kwargs)
		ctx['employee_list'] = Employee.objects.all()
		return ctx


# def get_week(request, year, month, day):
#	date = "{}-{}-{}".format(year,month,day)

#	hours = Hours_report.objects.filter(Week_of=date)

#	output={'hours':hours}

#	return render()

