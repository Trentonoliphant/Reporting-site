from django.contrib import admin

# Register your models here.
from Reports.models import Employee, Project, Hours_report

admin.site.register(Employee)
admin.site.register(Project)

class Hours_ReportAdmin(admin.ModelAdmin):
	list_display = ['Week_of','Employee','Project','Hours']
	list_filter = ['Week_of','Employee','Project']
	search_fields = ['Employee','Project']
admin.site.register(Hours_report, Hours_ReportAdmin)
