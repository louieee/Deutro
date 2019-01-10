from django.conf import settings
from django.db import models

from school.models import School
from student.models import genders
from subject.models import Subject

# Create your models here.

subjects = ((1, 'Elementary Science'), (2, 'Integrated Science'))


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    First_Name = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='images/', default=None)
    Last_Name = models.CharField(max_length=255)
    Gender = models.IntegerField(choices=genders)
    stage = models.IntegerField()
    subject = models.CharField(max_length=255)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
