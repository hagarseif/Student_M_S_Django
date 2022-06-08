from django.db import models

# Create your models here.


class subject(models.Model):
    subject_id=models.IntegerField(primary_key=True,auto_created=True)
    subject_name=models.CharField(max_length=50)
    updated_at=models.DateField(null=True)
    crated_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject_name

class student(models.Model):
    student_id=models.IntegerField(primary_key=True , auto_created=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    grade=models.IntegerField()
    email=models.EmailField(max_length=150)
    # study=models.ManyToManyField(subject)


    def __str__(self):
        return self.f_name

class result(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    degree=models.FloatField()
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)



class teacher(models.Model):
    t_id=models.IntegerField(primary_key=True,auto_created=True)
    t_name=models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    subject_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    teach=models.ManyToManyField(student)


    def __str__(self):
        return self.t_name









