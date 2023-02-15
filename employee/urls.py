

from django.urls import path
from . import views


app_name = "employee"


urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('userlogout',views.userlogout,name="userlogout"),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('userdesignation/',views.userdesignation,name='userdesignation'),
    path('userdesignation_list/',views.userdesignation_list,name='userdesignation_list'),
    path('userdepartment/',views.userdepartment,name='userdepartment'),
    path('userdepartment_list/',views.userdepartment_list,name='userdepartment_list'),
    path('useremployee_form/',views.useremployee_form,name='useremployee_form'),
    path('useremployee_list/',views.useremployee_list,name='useremployee_list'),
    path('userleave_form/',views.userleave_form,name='userleave_form'),
    path('userleave_list/',views.userleave_list,name='userleave_list'),
    path('userleave_type/',views.userleave_type,name='userleave_type'),
    path('userleave_type_list/',views.userleave_type_list,name='userleave_type_list'),
    path('userpuch_in/',views.userpuch_in,name='userpuch_in'),
    path('userpuch_out/<id>',views.userpuch_out,name='userpuch_out'),
    path('user_attendence/',views.user_attendence,name='user_attendence'),
    path('userleave_delete/<int:id>',views.userleave_delete,name="userleave_delete"),
    path('approvrd_reject/<int:id>/<str:start_date>',views.approvrd_reject,name="approvrd_reject"), 

   
    

    
]