from ast import Return
from urllib import request
from django.shortcuts import render

# Create your views here.

def homestudent(request):
    return render(request, 'Student/home.html')

def personaldate(request):
    return render(request, 'Student/personaldata.html')

def Homework(request):
    return render(request, 'Student/Homework.html')  

def timeTable(request):
    return render(request, 'Student/timeTable.html')

def result(request):
    return render(request, 'Student/result.html')

def academicreport(request):
    return render(request,'Student/academicreport.html')  

def behavioralreport(request):
    return render(request,'Student/behavioralreport.html')  

def take_attendence(request):
    return render(request,'Student/attendance.html')

def logout(request):
    return render(request,'Student/interface.html')    


from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import attendance,student


def retrievattendance(request):
    x = attendance.objects.all()

    return render(request, 'student/attendance.html' , {'attendance':x})


def retrievbehavioralreport(request):
    x = attendance.objects.all()

    return render(request, 'student/behavioralreport.html' , {'behavioralreport':x})

def retrievacademicreport(request):
    x = academicreport.objects.all()

    return render(request, 'student/academicreport.html' , {'academicreport':x})


def retrievpersonaldata(request):
    x = student.objects.all()

    return render(request, 'student/personaldata.html' , {'personaldatareport':x})





     

