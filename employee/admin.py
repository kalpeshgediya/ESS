



from django.contrib import admin
from .models import Employee,designation,department,leave_type,leave,attendence



class designation1(admin.ModelAdmin):
    list_display = ['designation_name']
admin.site.register(designation,designation1)


class department1(admin.ModelAdmin):
    list_display = ['department_name','code']
admin.site.register(department,department1) 


class leave_type1(admin.ModelAdmin):
    list_display = ['leave_name','max_leaves','carry_forword']
admin.site.register(leave_type,leave_type1)


class Employee1(admin.ModelAdmin):
    list_display = ['first_name','last_name','dob','address','phone_no','email','password','employee_designation','employee_department','acess_type','reporting_to']
admin.site.register(Employee,Employee1)

class leave1(admin.ModelAdmin):
    list_display = ['employee_name','start_date','end_date','leave_types','status','A_R_date']
admin.site.register(leave,leave1)

class attendence1(admin.ModelAdmin):
    list_display = ['employee_name','punch_in','punch_out','duration','date']
admin.site.register(attendence,attendence1)