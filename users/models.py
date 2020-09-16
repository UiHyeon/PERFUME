from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   username = models.CharField(default="username", max_length=64, null=True, blank=True)
   email = models.CharField(default="email", max_length=64)
   password = models.CharField(default="password", max_length=64)
   birth = models.CharField(default="birth", max_length=8, null=True)

   def __str__(self): 
        return self.email