from django.db import models

# Create your models here.

#creating a student model
class StudentModel(models.Model):
    Student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    marks = models.IntegerField()
    city = models.CharField(max_length=100)
    hosteler = models.BooleanField(default=False)

    