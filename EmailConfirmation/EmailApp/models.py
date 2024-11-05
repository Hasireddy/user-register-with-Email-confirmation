from django.db import models

from django.core import validators

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True,validators= [validators.EmailValidator(message="Invalid Email")])
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.first_name
