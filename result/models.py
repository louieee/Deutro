from django.db import models

from student.models import Student


# Create your models here.

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Year = models.PositiveIntegerField()
    First_term = models.FileField(upload_to='results/1st_term/', default=None)
    First_term_card = models.CharField(max_length=255, default=None)
    Second_term = models.FileField(upload_to='results/2nd_term/', default=None)
    Second_term_card = models.CharField(max_length=255, default=None)
    Third_term = models.FileField(upload_to='results/3rd_term/', default=None)
    Third_term_card = models.CharField(max_length=255, default=None)
