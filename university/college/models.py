from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Batch(models.Model):
    batch=models.CharField(max_length=255)
    def __str__(self):
          return self.batch


class Teacher(models.Model):
    name=models.CharField(max_length=255)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)  
    def _str_(self):
      return self.name


class Student(models.Model):
    name=models.CharField(max_length=255)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
