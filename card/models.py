from django.db import models


# Create your models here.

class Card(models.Model):
    code = models.CharField(max_length=20)
    year = models.IntegerField(default=0)
    student_id = models.IntegerField(default=0)
    term = models.IntegerField(default=0)
    used = models.BooleanField(default=False)

