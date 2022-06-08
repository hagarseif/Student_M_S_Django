from django.shortcuts import get_object_or_404, render

# Create your views here.
def showHome(request):
    return render(request, 'Admin_student/index.html')

def showmanage_staff(request):
    return render(request, 'Admin_student/manage_staff.html')


def showadd_staff(request):
    return render(request, 'Admin_student/add_staff.html')


def showadd_stu(request):
    return render(request, 'Admin_student/addstu.html')


def showmanage_student(request):
    return render(request, 'Admin_student/Manage_student.html')


def showmanage_subject(request):
    return render(request, 'Admin_student/manage-subject.html')


def showresult(request):
    return render(request, 'Admin_student/result.html')


def showview_attendance(request):
    return render(request, 'Admin_student/View_attendance.html')


def showinterface(request):
    return render(request, 'Admin_student/interface.html')


def showLogin(request):
    return render(request, 'Admin_student/login.html')

def showadd_subject(request):
    return render(request, 'Admin_student/add_subject.html')

from Admin_student import models
from .models import student,result

def view_result(request):
    s=models.result.objects.all()
    stu_id=None
    if 'id' in request.GET:
        stu_id =request.GET['id']
        # if  stu_id:
        s=s.filter(student_id=stu_id)
    context={
        'pro':s
    }
    return render(request, 'Admin_student/view_result.html',context)

# def view_result(request):
#
#     return render(request, 'Admin_student/view_result.html',{'pro':result.objects.filter(student_id=1)})

#
# def view_stu_att(request):
#     s = models.attendance.objects.all()
#     stu_id = None
#     if 's' in request.GET:
#         stu_id = request.GET['s']
#         if stu_id:
#             s = s.filter(student_id=stu_id)
#     context = {
#         'result': s
#     }
#     return render(request, 'Admin_student/attendance.html', context)
