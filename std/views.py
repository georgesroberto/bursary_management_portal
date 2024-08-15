from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bus.models import Bursary, Application
from std.models import Student
from bus.forms import ApplicationForm

# Create your views here.

def student_index(request):
    students = Student.objects.all()
    applications = Application.objects.all()
    context={'students':students,'applications':applications}
    return render(request, 'student/index.html', context)


# Student Views
def student_list(request):
    students = Student.objects.all()
    context ={'students':students}
    return render(request, 'student/student_list.html', context)

# Application Views
@login_required
def view_bursaries(request):
    bursaries = Bursary.objects.all().order_by('-created_at')
    students = Student.objects.all()
    return render(request, 'student/view_bursaries.html', {'bursaries': bursaries, 'students': students})

@login_required
def apply_for_bursary(request, bursary_id, student_id):
    bursary = get_object_or_404(Bursary, id=bursary_id)
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = student
            application.bursary = bursary
            application.status = 'Submitted'
            application.save()
            return redirect('application_list', application_id=application.id)
    else:
        form = ApplicationForm()

    return render(request, 'student/apply_for_bursary.html', {'form': form, 'bursary': bursary})

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'student/application_list.html', {'applications':applications})

@login_required
def view_application_status(request):
    student = request.user.student
    applications = Application.objects.filter(student=student)
    return render(request, 'student/application_status.html', {'applications': applications})


# Application Views
