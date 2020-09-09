from django.db import models

# Create your models here.
class Faculty(models.Model):
	branches = (('ece','ECE'),('cse', 'CSE'), ('it', 'IT'))

	First_name = models.CharField(max_length= 20)
	Last_name = models.CharField(max_length=20)
	Age = models.IntegerField()
	Email = models.EmailField()
	Department = models.CharField(max_length=10, choices=branches, default = '----')
	Join_Date = models.DateField(null=True)
	mobile = models.CharField(max_length=10, help_text='Enter 10 digit number')
	qualification = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.First_name
	class Meta:
		verbose_name_plural = 'Faculty'