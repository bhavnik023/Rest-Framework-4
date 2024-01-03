from django.db import models

# Create your models here.
class Demonstrate(models.Model):
	postId=models.CharField(max_length=10,blank=True)
	name=models.CharField(max_length=100,blank=True)
	email=models.EmailField(max_length=100,blank=True)
	body=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.name

