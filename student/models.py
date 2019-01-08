from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from school.models import School

# Create your models here.
genders = ((1, 'Male'), (2, 'Female'))


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Image = models.ImageField(upload_to='images/', default=None)
    Entry_year = models.PositiveIntegerField(validators=[MaxValueValidator(4)])
    Gender = models.IntegerField(choices=genders)
    is_primary = models.BooleanField(default=False)
    is_secondary = models.BooleanField(default=False)
    stage = models.PositiveIntegerField(validators=[MaxValueValidator(6)])
    Age = models.DateField()
    School = models.ForeignKey(School, on_delete=models.CASCADE)
