from django.db import models

from student.models import Student


# Create your models here.

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Year = models.PositiveIntegerField()
    _1st_term = models.FileField(upload_to='results/1st_term/', default=None)
    _2nd_term = models.FileField(upload_to='results/2nd_term/', default=None)
    _3rd_term = models.FileField(upload_to='results/3rd_term/', default=None)
