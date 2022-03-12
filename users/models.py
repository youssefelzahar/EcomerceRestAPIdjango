from django.contrib.auth.models import AbstractUser  
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

   
...
class Clothes (models.Model):
    title=models.CharField(max_length=30)
    describtion=models.CharField(max_length=30)
    Clothes_image = models.ImageField(upload_to='images/')
    price=models.IntegerField

class Hardware (models.Model):
    title=models.CharField(max_length=30)
    describtion=models.CharField(max_length=30)
    Hardware_iamge = models.ImageField(upload_to='images/')
    price=models.IntegerField

class Books (models.Model):
    title=models.CharField(max_length=30)
    describtion=models.CharField(max_length=30)
    Books_image = models.ImageField(upload_to='images/')
    price=models.IntegerField


