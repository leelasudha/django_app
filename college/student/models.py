from django.db import models

# Create your models here.
class Student(models.Model):
	First_name = models.CharField(max_length= 20)
	Last_name = models.CharField(max_length=20)
	Branch = models.CharField(max_length=10)
	Age = models.IntegerField()
	Email = models.EmailField()
