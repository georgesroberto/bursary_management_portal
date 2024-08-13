from django.db import models
from users.models import Person


class Institution(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_person = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'status': 'institution'})

    def __str__(self):
        return self.name 

class Student(Person):
    student_id = models.CharField(max_length=20, unique=True)
    # institution = models.ForeignKey('person.Institution', on_delete=models.CASCADE)
    program = models.CharField(max_length=100)
    year_of_study = models.IntegerField()

    def __str__(self):
        return self.username
