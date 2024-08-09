from django.db import models
from users.models import Person
from std.models import Student

class Bursary(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'status': 'cdf'})
    created_at = models.DateTimeField(auto_now_add=True)

class Questionnaire(models.Model):
    bursary = models.ForeignKey(Bursary, on_delete=models.CASCADE)
    question_text = models.TextField()

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bursary = models.ForeignKey(Bursary, on_delete=models.CASCADE)
    answers = models.JSONField()
    status = models.CharField(max_length=20, choices=[('Submitted', 'Submitted'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

class Document(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
