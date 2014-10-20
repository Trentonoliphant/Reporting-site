from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from Reports.models import Employee, Project

class ProjectsView(generic.ListView):
	template_name = 'Reports/projects.html'
	context_object_name = 'projects_list'

	def get_queryset(self):
		return Project.objects.all()

class DetailView(generic.DetailView):
	model = Project
	template_name = 'Reports/detail.html'

	context_object_name = 'project'

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

def Submit(request, project_id):
	p = get_object_or_404(Project, pk = project_id)
	choices = p.Employee.get(pk=request.POST['employee'])
	for choice in choices:
		project.Employee.add(choice)
	return HttpResponseRedirect(reverse('reports:edit', args=(project_id,)))
#def get_week(request, year, month, day):
#	date = "{}-{}-{}".format(year,month,day)

#	hours = Hours_report.objects.filter(Week_of=date)

#	output={'hours':hours}

#	return render()