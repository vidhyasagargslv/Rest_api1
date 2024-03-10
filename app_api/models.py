from django.db import models

# Create your models here.

#creating a student model
class TeachersModel(models.Model):
    
    RegNo = models.IntegerField()
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phone = models.IntegerField()
    Domian =models.CharField(max_length=100)

    