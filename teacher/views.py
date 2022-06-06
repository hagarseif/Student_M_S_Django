from django.shortcuts import render

# Create your views here.
def addacademicreport(request):
    return render(request,'teacher/add academic report.html')
def addbehavioralreport(request):
    return render(request,'teacher/add behavioral report.html')    
def addtimetable(request):
    return render(request,'teacher/add_timeTable.html')
def adddhomework(request):
    return render(request,'teacher/addd_homework.html')    
def home(request):
    return render(request,'teacher/home.html')
def showLogin(request):
    return render(request, 'teacher/login.html')

def takeatt(request):
    return render(request,'teacher/take_att.html')
def viewatt(request):
    return render(request,'teacher/view_att.html')
def viewstudent(request):
    return render(request,'teacher/view_student.html')

def showinterface(request):
    return render(request, 'teacher/interface.html')