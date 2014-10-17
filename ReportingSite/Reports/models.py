from django.db import models
from datetime import datetime

# Create your models here.

class Employee(models.Model):
	employee_name = models.CharField(max_length = 200)
	weekly_hours = models.IntegerField(default = 0)
	def __str__(self):
		return self.employee_name

class Project(models.Model):
	project_name = models.CharField(max_length = 200)
	total_hours = models.IntegerField(default = 0)

	def __str__(self):
		return self.project_name

class Hours_report(models.Model):
	Employee = models.ForeignKey(Employee)
	Project = models.ForeignKey(Project)
	Hours = models.IntegerField(default = 0)
	Week_of = models.DateField('reporting week', default = datetime.now())
	
	def __str__(self):
		return str(self.Week_of.strftime("%B %d %Y"))

class Weekly_report(models.Model):
	report_name = models.CharField(max_length = 200, null=True)
	Employee = models.ManyToManyField(Employee)
	Project = models.ManyToManyField(Project)
	reporting_week = models.DateField('reporting week', default = datetime.now())
	
	def __str__(self):
		return '{} report for week starting on {}'.format(self.report_name, self.reporting_week.strftime("%B %d %Y"))