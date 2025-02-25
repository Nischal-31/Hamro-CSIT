from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    terms_agree = models.BooleanField(default=False)
    remember_me = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

