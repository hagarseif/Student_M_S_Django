from django.contrib import admin
from .models import student,subject,result,teacher,attendance

# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(result)
admin.site.register(teacher)
admin.site.register(attendance)
