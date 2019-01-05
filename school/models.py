from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.URLField()
    email = models.EmailField()
    motto = models.CharField(max_length=255, default=None)
    Image = models.ImageField(upload_to='images/', default=None)
