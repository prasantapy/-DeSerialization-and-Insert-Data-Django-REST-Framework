from django.db import models

# Create your models here.
class Student_model(models.Model):
    name=models.CharField(max_length=30)
    rollnumber=models.IntegerField()
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)