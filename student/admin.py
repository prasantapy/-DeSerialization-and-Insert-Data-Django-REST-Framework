from django.contrib import admin
from .models import Student_model
# Register your models here.
@admin.register(Student_model)
class student_admin(admin.ModelAdmin):
    list_display=['id','name','rollnumber','email','password']