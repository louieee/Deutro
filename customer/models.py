from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customer(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


