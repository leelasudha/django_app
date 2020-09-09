from django.db import models

# Create your models here.
class Student(models.Model):
	First_name = models.CharField(max_length= 20)
	Last_name = models.CharField(max_length=20)
	Branch = models.CharField(max_length=10)
	Age = models.IntegerField()
	Email = models.EmailField()

class LoginUser(models.Model):
	fname= models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	username= models.CharField(max_length=50, unique=True)
	email = models.EmailField(max_length=50, unique=True)
	dob = models.DateField(null=True)
	password = models.CharField(max_length=50)

