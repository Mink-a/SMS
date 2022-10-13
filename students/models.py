from contextlib import nullcontext
from email.policy import default
from django.db import models

# Create your models here.


class Student(models.Model):
    student_number = models.PositiveBigIntegerField(default=1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField(default=0.0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.student_number}: {self.first_name} {self.last_name}'
