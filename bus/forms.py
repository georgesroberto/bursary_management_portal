from django import forms
from .models import Bursary, Application

class BursaryForm(forms.ModelForm):
    class Meta:
        model = Bursary
        fields = ['title', 'description', 'amount']

    def __init__(self, *args, **kwargs):
        super(BursaryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = 'status',
