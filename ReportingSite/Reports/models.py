from django.db import models
from datetime import datetime

# Create your models here.

class Employee(models.Model):
	Employee_name = models.CharField(max_length = 200)
	Available_hours = models.IntegerField(default = 40)
	Worked_hours = 0

	def calculate_worked_hours(self):
		self.Worked_hours = 0
		for hours_report in self.hours_report_set.all():
			self.Worked_hours += hours_report.Hours
		return self.Worked_hours

	def __str__(self):
		return self.Employee_name



class Project(models.Model):
	Employee = models.ManyToManyField(Employee)
	Project_name = models.CharField(max_length = 200)
	total_hours = 0

	def calculate_total_hours(self):
		self.total_hours = 0
		for hours_report in self.hours_report_set.all():
			self.total_hours += hours_report.Hours
		return self.total_hours

	def __str__(self):
		return self.Project_name



class Hours_report(models.Model):
	Employee = models.ForeignKey(Employee)
	Project = models.ForeignKey(Project)
	Hours = models.IntegerField(default = 0)
	Week_of = models.DateField('reporting week', default = datetime.now())
	
	def __str__(self):
		return str(self.Week_of.strftime("%B %d %Y"))
		


