from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bus.models import Bursary, Application
from bus.forms import QuestionnaireForm
from std.models import Student


# Create your views here.

# Student Views
def student_list(request):
    students = Student.objects.all()
    context ={'students':students}
    return render(request, 'student/student_list.html', context)

# Application Views
@login_required
def view_bursaries(request):
    bursaries = Bursary.objects.all().order_by('-created_at')
    return render(request, 'student/view_bursaries.html', {'bursaries': bursaries})

@login_required
def apply_for_bursary(request, bursary_id):
    bursary = get_object_or_404(Bursary, id=bursary_id)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student
            application.bursary = bursary
            application.save()
            return redirect('application_status', application_id=application.id)
    else:
        form = QuestionnaireForm()
    return render(request, 'student/apply_for_bursary.html', {'form': form, 'bursary': bursary})



def application_index(request):
    bursaries = Bursary.objects.all()
    return render(request, 'student/index.html', {'bursaries':bursaries})

@login_required
def view_application_status(request):
    student = request.user.student
    applications = Application.objects.filter(student=student)
    return render(request, 'student/application_status.html', {'applications': applications})


# Application Views
