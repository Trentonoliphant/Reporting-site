from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from Reports.models import Weekly_report, Hours_report

class ReportView(generic.ListView):
	template_name = 'Reports/reports.html'
	context_object_name = 'reports_list'

	def get_queryset(self):
		return Weekly_report.objects.all()

class DetailView(generic.ListView):
	model = Hours_report
	template_name = 'Reports/detail.html'

	context_object_name = 'report'

	def get_queryset(self):
		weeks = {'4':'2014-10-01','3':'2014-10-14'}

		week = weeks[self.kwargs['pk']]
		return Hours_report.objects.filter(Week_of=week).order_by('Employee')


def get_week(request, year, month, day):
	date = "{}-{}-{}".format(year,month,day)

	hours = Hours_report.objects.filter(Week_of=date)

	output={'hours':hours}

	return render()