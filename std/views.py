from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bus.models import Bursary, Application
from .forms import StudentRegistrationForm, BursaryApplicationForm, InstitutionForm


# Create your views here.
def index(request):
    return HttpResponse('Home')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('profile')
    else:
        form = StudentRegistrationForm()
    return render(request, 'student/register.html', {'form': form})

def register_institution(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('institution_list')
    else:
        form = InstitutionForm()
    return render(request, 'student/register_institution.html', {'form': form})

@login_required
def view_bursaries(request):
    bursaries = Bursary.objects.all()
    return render(request, 'student/view_bursaries.html', {'bursaries': bursaries})

@login_required
def apply_for_bursary(request, bursary_id):
    bursary = get_object_or_404(Bursary, id=bursary_id)
    if request.method == 'POST':
        form = BursaryApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student
            application.bursary = bursary
            application.save()
            return redirect('application_status', application_id=application.id)
    else:
        form = BursaryApplicationForm()
    return render(request, 'student/apply_for_bursary.html', {'form': form, 'bursary': bursary})

@login_required
def view_application_status(request):
    student = request.user.student
    applications = Application.objects.filter(student=student)
    return render(request, 'student/application_status.html', {'applications': applications})
