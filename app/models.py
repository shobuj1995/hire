from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    gender = models.CharField(null=False,blank=False,default=None,max_length=20)
    user_type = models.CharField(null=False,blank=False,default=None,max_length=20)
    mobile_no = models.CharField(null=False,blank=False,default=None,max_length=20)



    def __str__(self):
        return self.email
