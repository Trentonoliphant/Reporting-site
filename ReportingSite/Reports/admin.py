from django.contrib import admin

# Register your models here.
from Reports.models import Employee, Project, Weekly_report, Hours_report

admin.site.register(Employee)
admin.site.register(Project)

class Hours_report_Admin(admin.ModelAdmin):
	list_display = ['Week_of','Employee','Project']
	list_filter = ['Week_of', 'Employee', 'Project']
admin.site.register(Hours_report, Hours_report_Admin)

class Weekly_report_admin(admin.ModelAdmin):
	fieldsets = [(None, {'fields':['reporting_week','Employee','Project', 'report_name']})]
	list_display = ['report_name','reporting_week']
	list_filter = ['reporting_week','report_name']
	search_fields = ['reporting_week','report_name']
admin.site.register(Weekly_report, Weekly_report_admin)