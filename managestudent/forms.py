from dataclasses import fields
from django import forms 

from .models import attendance , behavioralreport , personaldata

class StudentForm(forms.ModelForm):
    class Meta:
        model = attendance
        fields = '__all__'