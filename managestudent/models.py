from django.db import models

# Create your models here.




class attendance(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    class_id = models.IntegerField(primary_key=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) -> str:
        return self.code





   

class student(models.Model):
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    


    def __str__(self) -> str:
        return self.code