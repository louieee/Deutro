from django.db import models


# Create your models here.

class Card(models.Model):
    code = models.CharField(max_length=20)
