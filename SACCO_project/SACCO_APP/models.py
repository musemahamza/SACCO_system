from django.db import models

# Create your models here.
class loans(models.Model):
	firstname=models.CharField(max_length=100)
	middlename=models.CharField(max_length=100, blank=True)
	lastname=models.CharField(max_length=100)
	contact_no=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	g_name=models.CharField(max_length=100)
	phone_number=models.CharField(max_length=100)
	g_address=models.CharField(max_length=100)
	# starttime= models.TimeField()
	# endtime= models.TimeField()

	# renames the instances of the model
	# with their title name
	# def __str__(self):
	# 	return self.title