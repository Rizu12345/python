from django.contrib import admin
from .models import *

# Register your models here.

class Department_display(admin.ModelAdmin):
    list_display=['name']



class batch_display(admin.ModelAdmin):
    list_display=['batch']


class teacher_display(admin.ModelAdmin):
    list_display=['name','dept']
          
class student_display(admin.ModelAdmin):
    list_display=['name','batch','teacher']




admin.site.register(Department,Department_display)
admin.site.register(Batch,batch_display)
admin.site.register(Teacher,teacher_display)
admin.site.register(Student,student_display)


