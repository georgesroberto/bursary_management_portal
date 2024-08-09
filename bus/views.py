# Import statements

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.decorators import check_group_permission
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from .models import Bursary, Questionnaire, Application, Document
from .forms import BursaryForm, QuestionnaireForm, ApplicationForm


# Create your views here.
@check_group_permission(['Checklist', 'Administrator'])
def index(request):
    return HttpResponse('Home')

# Bursary Views

def bursary_list(request):
    query = request.GET.get('q')
    if query:
        bursaries = Bursary.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        bursaries = Bursary.objects.all()
    return render(request, 'bursary/bursary_list.html', {'bursaries': bursaries})


@login_required
def create_bursary(request):
    if request.method == 'POST':
        form = BursaryForm(request.POST)
        if form.is_valid():
            bursary = form.save(commit=False)
            bursary.posted_by = request.user
            bursary.save()
            messages.success(request, 'Bursary created successfully.')
            return redirect('bursary_list')
    else:
        form = BursaryForm()
    return render(request, 'bursary/create_bursary.html', {'form': form})


@login_required
def issue_bursary(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.user.status == 'cdf' and application.status == 'Approved':
        # Generate and attach document logic here
        doc = Document.objects.create(application=application)
        # Generate PDF or other document here
        messages.success(request, 'Bursary issued and document generated.')
        return redirect('application_status', application_id=application.id)
    return redirect('bursary_list')


# Questionnaire Views

@login_required
def create_questionnaire(request, bursary_id):
    bursary = get_object_or_404(Bursary, id=bursary_id)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            questionnaire.bursary = bursary
            questionnaire.save()
            messages.success(request, 'Questionnaire created successfully.')
            return redirect('bursary_detail', bursary_id=bursary.id)
    else:
        form = QuestionnaireForm()
    return render(request, 'bursary/create_questionnaire.html', {'form': form, 'bursary': bursary})


#  Application views

@login_required
def submit_application(request, bursary_id):
    bursary = get_object_or_404(Bursary, id=bursary_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student
            application.bursary = bursary
            application.save()
            messages.success(request, 'Application submitted successfully.')
            return redirect('application_status', application_id=application.id)
    else:
        form = ApplicationForm()
    return render(request, 'bursary/submit_application.html', {'form': form, 'bursary': bursary})


@login_required
def application_detail(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'bursary/application_detail.html', {'application': application})

