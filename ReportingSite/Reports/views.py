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

class DetailView(generic.ListView):
	
	template_name = 'Reports/detail.html'

	context_object_name = 'Project'

	def get_context_data(self, **kwargs):
		ctx = super(DetailView, self).get_context_data(**kwargs)
		ctx['Employee'] = Employee.objects.all()
		ctx['Hours_report'] = Hours_report.objects.all().order_by('Project')
		return ctx

	def get_queryset(self):
		return Project.objects.all()
	#def get_queryset(self):
	#	weeks = {'4':'2014-10-01','3':'2014-10-14'}

	#	week = weeks[self.kwargs['pk']]
	#	return .objects.filter(Week_of=week).order_by('Employee')

class EditView(generic.DetailView):
	model = Project
	template_name = 'Reports/edit.html'
	context_object_name = 'project'

	def get_context_data(self, **kwargs):
		ctx = super(EditView, self).get_context_data(**kwargs)
		ctx['employee_list'] = Employee.objects.all()
		return ctx

class MonthView(generic.ListView):
	template_name = 'Reports/month.html'
	months = [calendar.month_name[i] for i in range(1, 13)]
	context_object_name ='Month_list'
	
	def get_queryset(self):
		return self.months


# def Submit(request, project_id):
# 	project = Project.objects.get(pk=project_id)
# 	choice_list = []
# 	if request.POST['employee']:
# 		for key in request.POST['employee']:
# 			choice_list.append(key)
# 		for choice in choice_list:
# 			project.Employee.add(choice)
# 			project.save()
# 		return HttpResponseRedirect(reverse('reports:edit',args=(project_id,)))


# def get_week(request, year, month, day):
#	date = "{}-{}-{}".format(year,month,day)

#	hours = Hours_report.objects.filter(Week_of=date)

#	output={'hours':hours}

#	return render()

