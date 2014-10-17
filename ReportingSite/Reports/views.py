from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from Reports.models import Weekly_report, Hourly_report

class ReportView(generic.ListView):
	template_name = 'Reports/reports.html'
	context_object_name = 'reports_list'

	def get_queryset(self):
		return Weekly_report.objects.all()

class DetailView(generic.DetailView):
	model = Weekly_report
	template_name = 'Reports/detail.html'

	context_object_name = 'report'

class HoursView(generic.DetailView):
	model = Hourly_report
	