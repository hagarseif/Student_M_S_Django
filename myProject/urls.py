"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Admin_student.views import showHome
from Admin_student.views import showmanage_staff
from Admin_student.views import showadd_staff
from Admin_student.views import showLogin
from Admin_student.views import showadd_stu
from Admin_student.views import showresult
from Admin_student.views import showmanage_student
from Admin_student.views import showview_attendance
from Admin_student.views import showadd_subject
from Admin_student.views import showmanage_subject
from Admin_student.views import showinterface,view_result,view_stu_att
from teacher.views import addacademicreport,\
    addbehavioralreport, adddhomework, addtimetable, \
    home, takeatt, viewatt, viewstudent ,showLogin


from managestudent.views import personaldate
from managestudent.views import Homework
from managestudent.views import timeTable
from managestudent.views import result
from managestudent.views import academicreport
from managestudent.views import behavioralreport
from managestudent.views import take_attendence
from managestudent.views import logout ,homestudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_home/', showHome),
    path('admin_home/showMstaff', showmanage_staff),
    path('admin_home/showAstaff', showadd_staff),
    path('admin_home/showlogin', showLogin),
    path('admin_home/showAstu', showadd_stu),
    path('admin_home/showresult', showresult),
    path('admin_home/showMstudent', showmanage_student),
    path('admin_home/showVattendance', showview_attendance),
    path('admin_home/showAsubject', showadd_subject),
    path('admin_home/showMsubject', showmanage_subject),
    path('admin_home/showinterface', showinterface),
    path('admin_home/view_result', view_result ,name='view_result'),
    path('admin_home/view_stu_att', view_stu_att, name='view_stu_att'),

    path('teacher_home/', home),
    path('teacher_home/addacademicreport', addacademicreport),
    path('teacher_home/addbehavioralreport', addbehavioralreport),
    path('teacher_home/addtimetable', addtimetable),
    path('teacher_home/addhomework', adddhomework),
    path('teacher_home/takeatt', takeatt),
    path('teacher_home/viewatt', viewatt),
    path('teacher_home/viewstudent', viewstudent),
    path('teacher_home/showinterface', showinterface),
    path('teacher_home/showlogin', showLogin),

    path('student_home/', homestudent),
    path('student_home/personaldata', personaldate),
    path('student_home/Homework', Homework),
    path('student_home/timeTable', timeTable),
    path('student_home/result', result),
    path('student_home/academicreport', academicreport),
    path('student_home/behavioralreport', behavioralreport),
    path('student_home/take_attendence', take_attendence),
    path('student_home/showinterface', logout),
    path('student_home/showlogin', showLogin),


]
