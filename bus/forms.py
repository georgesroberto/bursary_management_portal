from django import forms
from .models import Bursary, Questionnaire, Application

class BursaryForm(forms.ModelForm):
    class Meta:
        model = Bursary
        fields = ['title', 'description', 'amount']

class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question_text']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['answers']
