from django.db import models

# Create your models here.
class student(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)

    def __str__(self):
        return self.f_name

class subject(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class results(models.Model):
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    result=models.IntegerField()

    def __str__(self):
        return self. student_id

class attendance(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id


