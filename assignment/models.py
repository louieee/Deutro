from django.core.validators import MaxValueValidator
from django.db import models

from school.models import School
from teacher.models import subjects


# Create your models here.

class Assignment(models.Model):
    date_given = models.DateTimeField()
    submission_date = models.DateTimeField()
    subject = models.IntegerField(choices=subjects)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default=None)
    file = models.FileField(upload_to='assignments/', default=None)
    stage = models.PositiveIntegerField(validators=[MaxValueValidator(6)])
    school = models.ForeignKey(School, on_delete=models.CASCADE)
