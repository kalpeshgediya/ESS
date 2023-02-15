from django.db import models
from django.contrib.auth.models import User


class designation(models.Model):
    designation_name = models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name
    
class department(models.Model):
    department_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='employee_user')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    phone_no = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=12)
    employee_designation = models.ForeignKey(designation,on_delete=models.CASCADE)
    employee_department = models.ForeignKey(department,on_delete=models.CASCADE)
    access_status = (
        ('A','Admin'),
        ('E','Employee')
    )
    acess_type = models.CharField(max_length=20,choices=access_status)
    reporting_to = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.first_name

class leave_type(models.Model):
    leave_name = models.CharField(max_length=100)
    max_leaves = models.IntegerField()
    CARRY_STATUS = (
        ('1','Yes'),
        ('2','No')
    ) 
    carry_forword = models.CharField(max_length=20,choices=CARRY_STATUS)

    def __str__(self):
        return self.leave_name

class leave(models.Model):
    employee_name = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_leave')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_types = models.ForeignKey(leave_type,on_delete=models.CASCADE)
    LEAVE_STATUS = (
        ('1','Approved'),
        ('2','Rejected')
    ) 
    status = models.CharField(max_length=20,choices=LEAVE_STATUS,blank=True,null=True)
    A_R_date  = models.DateField(blank=True,null=True)


class attendence(models.Model):
    employee_name =  models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True,related_name='employee_attendence')
    punch_in = models.TimeField()
    punch_out = models.TimeField(null=True)
    date =  models.DateField()
    duration = models.TimeField(blank=True,null=True)