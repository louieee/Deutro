from django.db import models


# Create your models here.

class Card(models.Model):
    code = models.CharField(max_length=20)
    Expiry = models.PositiveIntegerField(default=5)
