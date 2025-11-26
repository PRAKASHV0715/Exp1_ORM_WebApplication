from django.db import models
from django.contrib import admin
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the student's full name")
    age = models.IntegerField(help_text="Enter the student's age")
    date = models.DateField(help_text="Enter the date of enrollment")

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'date']    
