from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.

class Assignment(models.Model):
    date_given = models.DateTimeField()
    submission_date = models.DateTimeField()
    subject = models.CharField(max_length=255)
    file = models.FileField(upload_to='assignments/')
    stage = models.PositiveIntegerField(validators=[MaxValueValidator(6)])
