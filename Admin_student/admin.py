from django.contrib import admin
from .models import student,subject,result,teacher

# Register your models here.
admin.site.register(student)
admin.site.register(subject)
admin.site.register(result)
admin.site.register(teacher)
