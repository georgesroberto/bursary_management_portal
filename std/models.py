# models.py

from django.db import models
from users.models import Person

class Institution(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'status': 'institution'})

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)  # Reference to Institution model
    program = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.student_id
