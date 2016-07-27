from django.contrib import admin
from .models import Employee, Membership, Workplace

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('personal_number', 'last_name', 'first_name', 'main_workplace')
    ordering = ['last_name']
class WorkplaceAdmin(admin.ModelAdmin):
    def employeelist(self, workplace):
        employees = []
        # Needs to list several employees, currently lists one for unknown reason
        for employee in workplace.workers.all():
            employees.append(employee.last_name)
        return ' '.join(employees)
    employeelist.short_description = 'Employees'
    list_display = ('name','description','work_area','employeelist')
    ordering = ['name']
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('worker','workgroup','get_competence') 
    list_filter = ('worker','workgroup')
    def get_competence(self, obj):
        return str(obj.competence) + ' %'
    get_competence.short_description = 'Competence'

admin.site.register(Employee, WorkerAdmin)
admin.site.register(Membership,MembershipAdmin)
admin.site.register(Workplace,WorkplaceAdmin)
