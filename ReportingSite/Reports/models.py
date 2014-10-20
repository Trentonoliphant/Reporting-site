from django.db import models
from datetime import datetime

# Create your models here.

class Employee(models.Model):
	Employee_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.Employee_name

class Project(models.Model):
	Employee = models.ManyToManyField(Employee)
	Project_name = models.CharField(max_length = 200)
	total_hours = models.IntegerField(default = 0)

	def __str__(self):
		return self.Project_name