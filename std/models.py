from django.db import models
from users.models import Person

class Institution(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'status': 'institution'})

class Student(models.Model):
    registration_number = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
