from django.contrib.auth.models import AbstractUser
from django.db import models

class Person(AbstractUser):
    STATUS_CHOICES = [
        ('admin', 'Admin'),
        ('cdf', 'CDF'),
        ('institution', 'Institution'),
        ('student', 'Student'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.username}"



class UserProfile(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
