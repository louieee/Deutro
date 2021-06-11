from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Choice:
    class Gender:
        male, female = range(2)
    gender = ((Gender.male, 'male'), (Gender.female, 'female'))


class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    date_of_birth = models.DateField(default=None, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=Choice.gender, null=True, default=None)
    contact_info = models.ManyToManyField('users.Contact')

    def __str__(self):
        return self.username


