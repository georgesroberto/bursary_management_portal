from django import forms
from .models import Student, Institution
from bus.models import Application


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'program', 'year_of_study']

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'address', 'contact_person']

class BursaryApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['answers']