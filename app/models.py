from django.db import models

# Create your models here.
class user(models.Model):
	user_name=models.CharField(max_length=200)
	user_email=models.CharField(max_length=200)
	user_contact=models.CharField(max_length=200)
	user_password=models.CharField(max_length=200)
	user_desc = models.CharField(max_length=200)  