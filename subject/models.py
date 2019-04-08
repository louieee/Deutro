from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    for_primary = models.BooleanField(default=False)
    for_secondary = models.BooleanField(default=False)
