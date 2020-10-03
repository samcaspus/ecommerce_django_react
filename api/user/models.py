from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50,default='None')
    email = models.EmailField(max_length=200,unique=True)
    # password = models.PasswordField(max_length=200,required=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []    

    phone = models.CharField(max_length=20,blank=True,null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)

    session_token = models.CharField(max_length=10,default=0)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    

