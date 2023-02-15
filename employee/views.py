from django.shortcuts import render
from datetime import date, datetime, timezone
from pytz import timezone
from django.shortcuts import render,redirect
from .models import Employee, department, designation,leave_type,leave,attendence
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required




@login_required(login_url='/')
def useremployee_form(request):
    if request.user.is_superuser == True:
        designation_var = designation.objects.all()
        department_var = department.objects.all()
        first_name = Employee.objects.all()
        data = {
            'designation_var':designation_var,
            'department_var':department_var,
            'first_name':first_name
        }
        if request.method=="POST":
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            dob=request.POST['dob']
            address=request.POST['adress']
            email=request.POST['email']
            phone_no=request.POST['phone']
            password=request.POST['password']
            employee_designation=request.POST['designation']
            employee_department=request.POST['department']
            access_type=request.POST['access_type']
            if access_type == 'Admin':
                a = 'A'
            else:
                a = 'E'
            reporting_to=request.POST['reporting']

            designation_name = designation.objects.get(designation_name=employee_designation)
            department_name = department.objects.get(department_name=employee_department)
            if reporting_to != 'None':
                reporting_name = Employee.objects.get(first_name=reporting_to)
            if reporting_to != 'None':
                user = User.objects.create(username=email,email=email)
                data=Employee.objects.create(first_name=firstname,last_name=lastname,dob=dob,address=address,phone_no=phone_no,
                        email=email,employee_designation=designation_name,
                        employee_department=department_name,acess_type=a,reporting_to=reporting_name,user=user)
                data.password=make_password(password=password)
                user.password=make_password(password=password)
                data.save()
                user.save()
                print("data-------------------------",data)
            else:
                user = User.objects.create(username=email,email=email)
                data=Employee.objects.create(first_name=firstname,last_name=lastname,dob=dob,address=address,phone_no=phone_no,
                        email=email,employee_designation=designation_name,
                        employee_department=department_name,acess_type=a,user=user)
                data.password=make_password(password=password)
                user.password=make_password(password=password)
                data.save()
                user.save()
                print("data-------------------------",data)
                    
            return redirect('employee:useremployee_list')
        else:
            return render(request,"employee folder/employee_form.html",data)
    else:
        print("tesfkdsfdsf=====================",request.user.is_superuser)
        return redirect('employee:useremployee_list')
    
@login_required(login_url='/') 
def useremployee_list(request):
    data = Employee.objects.all()
    return render(request,"employee folder/employee_list.html",{'data':data}) 

def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print("user---------------",user)
        
        if user is not None:
            login(request,user) 
            messages.success(request,"login sucessfully")
            return redirect("employee:userdashboard")
        else:
            messages.warning(request,"Please Enter Email And Password")
            return render(request,"login.html")
    else:
        return render(request,"login.html")

@login_required(login_url='/')
def userdesignation(request):
        if request.method=="POST":
            designation_name=request.POST['name']
            data=designation(designation_name=designation_name)
            data.save() 
            print("data-------------------------",data)
            return redirect('employee:userdesignation_list')
        return render(request,"designation folder/designation.html")



@login_required(login_url='/')
def userdepartment(request):
    if request.method=="POST":
        department_name=request.POST['dname']
        code=request.POST['dcode']
        data=department(department_name=department_name,code=code)
        data.save()
        print("data-------------------------",data)
        return redirect("employee:userdepartment_list")
    return render(request,"department folder/department.html")

@login_required(login_url='/')
def userdepartment_list(request):
    data = department.objects.all()
    return render(request,"department folder/department_list.html",{'data':data})

@login_required(login_url='/')
def userleave_type(request):
    if request.method=="POST":
        Leave_Name=request.POST['Leave_Name']
        Max_Leaves=request.POST['Max_Leaves']
        Carry_Forword=request.POST['Carry_Forword']
        if Carry_Forword == 'yes':
            a = '1'
        else:
            a = '2'
        data=leave_type.objects.create(leave_name=Leave_Name,max_leaves=Max_Leaves,carry_forword=a)
        data.save()
        print("data-------------------------",data)
        return redirect("employee:userleave_type_list")
    return render(request,"leave_type folder/leave_type.html")

@login_required(login_url='/')
def userleave_type_list(request):
    data = leave_type.objects.all()
    return render(request,"leave_type folder/leave_type_list.html",{'data':data})

@login_required(login_url='/')
def userleave_form(request):
    e_first_name = Employee.objects.all()
    leave_name = leave_type.objects.all()
    data = {
            'e_first_name':e_first_name,
            'leave_name':leave_name
    }
    if request.method == "POST":
        e_name=request.POST['E_name']
        sdate=request.POST['sdate']
        edate=request.POST['edate']
        ltype=request.POST['ltype']


        employee_name = Employee.objects.get(first_name=e_name)
        leave_type_name = leave_type.objects.get(leave_name=ltype)
        data=leave.objects.create(employee_name=employee_name,start_date=sdate,end_date=edate,leave_types=leave_type_name)
        data.save()
        print("data-------------------------",data)
        return redirect("employee:userleave_list")
    else:
        return render(request,"leave folder/leave_form.html",data)

@login_required(login_url='/')
def userleave_list(request):
    data = leave.objects.all()
    
    return render(request,"leave folder/leave_list.html",{'data':data})

@login_required(login_url='/')
def userleave_delete(request,id): 
    leave.objects.get(id=id).delete()
    return redirect('employee:userleave_list')


@login_required(login_url='/')
def approvrd_reject(request,id,start_date):
    data = leave.objects.all()
    if 'Approve' in request.POST:
        a='1'
        print('a==================',a)
        data=leave.objects.filter(id=id,start_date=start_date) 
        data.update(status=a)
        # data.save()
        print('a==================',data)
        return redirect('employee:userleave_list') 
    
    if 'Rejecte' in request.POST:
        a='2'
        print('a==================',a)
        data=leave.objects.filter(id=id,start_date=start_date) 
        data.update(status=a)
        # data.save()
        print('a==================',data)
        return redirect('employee:userleave_list')
    return render(request,"leave folder/leave_list.html",{'data':data})



@login_required(login_url='/')
def userpuch_in(request):
    puchin = datetime.now(timezone("Asia/Kolkata"))
    print(puchin,'=======')
    dgfdsg = puchin.strftime('%H:%M:%S.%f')
    print(dgfdsg,'=======')
    today = date.today()
    print(5555555555555, request.user)
    user = User.objects.get(id=request.user.id)
    print(66666666666666666, user.employee_user)
    data=attendence.objects.create(punch_in=puchin,date=today,employee_name=user.employee_user)   
    return redirect(f"/userdashboard/?attendance_id={data.id}")

@login_required(login_url='/')
def userpuch_out(request,id):
    data=attendence.objects.filter(id=id)
    puchout = datetime.now(timezone("Asia/Kolkata")).time()
    print(00000000000000000000, id, data)
    # dgfdsg = puchout.strftime('%H:%M:%S.%f')
    print(1111111111111111111111111111, puchout)
    data.update(punch_out=puchout)
    print(22222222222222222222222, data)
    return redirect("employee:userdashboard")


@login_required(login_url='/')
def userdashboard(request):
    if request.user.is_superuser == False:
        print(request.user,'===============================')
        p_in = request.user.employee_user.employee_attendence.all()
        print(33333333333333333333,p_in) 
        punch_in_out_time = attendence.objects.all()
        attendance_ids = request.GET.get('attendance_id')
    
        data = {'attendance_ids':attendance_ids,
                'punch_in_out_time':punch_in_out_time,
                'p_in':p_in,
                }
        print(44444444444444444, attendance_ids)
        return render(request,"dashboard.html", context=data)
    else:
        return redirect('employee:useremployee_list')


def userlogout(request):
    logout(request)
    print(logout,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    return redirect("employee:userlogin")

@login_required(login_url='/')
def user_attendence(request):
    punch_in_out = attendence.objects.all()
    return render(request,"attendence.html",{'punch_in_out':punch_in_out})


@login_required(login_url='/')
def userdesignation_list(request):
    data = designation.objects.all()
    return render(request,"designation folder/designation_list.html",{'data':data})