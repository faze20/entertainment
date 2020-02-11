from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    address = models.CharField(max_length=201)
    telephone = models.CharField(max_length=12)


    