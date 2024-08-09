
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person

class UserRegistrationForm(UserCreationForm):
    STATUS_CHOICES = [
        ('admin', 'Admin'),
        ('cdf', 'CDF'),
        ('institution', 'Institution'),
        ('student', 'Student'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Person
        fields = ['username', 'first_name', 'last_name', 'email', 'status', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
