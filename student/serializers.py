from rest_framework import serializers
from .models import Student_model
class Student_serializers(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    rollnumber=serializers.IntegerField() 
    email=serializers.EmailField(max_length=30)
    password=serializers.CharField(max_length=30)

    def create(self,validate_date):
        return Student_model.objects.create(**validate_date)
