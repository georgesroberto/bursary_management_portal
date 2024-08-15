# Import statements

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.decorators import check_group_permission
from django.contrib import messages
from django.db.models import Q
from .models import Bursary, Application, Document
from .forms import BursaryForm, ApplicationForm


# Create your views here.
# @check_group_permission(['Checklist', 'Administrator'])
def bursary_index(request):
    bursaries = Bursary.objects.all()
    return render(request, 'bursary/index.html', {'bursaries':bursaries})

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
            return redirect('bus:list_bursaries')
    else:
        form = BursaryForm()
    return render(request, 'bursary/create_bursary.html', {'form': form, 'title':'Add '})


@login_required
def update_bursary(request, bursary_id):
    bursary = get_object_or_404(Bursary, pk=bursary_id)
    
    if request.method == 'POST':
        form = BursaryForm(request.POST, instance=bursary)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bursary updated successfully.')
            return redirect('bus:list_bursaries')
    else:
        form = BursaryForm(instance=bursary)
    
    return render(request, 'bursary/create_bursary.html', {'form': form, 'title':'Update '})


@login_required
def delete_bursary(request, bursary_id):
    bursary = get_object_or_404(Bursary, pk=bursary_id)
    
    if request.method == 'POST':
        bursary.delete()
        messages.success(request, 'Bursary deleted successfully.')
        return redirect('bus:list_bursaries')   
    return render(request, 'bursary/confirm_delete_bursary.html', {'bursary': bursary})


@login_required
def issue_bursary(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.user.status == 'cdf' and application.status == 'Approved':
        # Generate and attach document logic here
        doc = Document.objects.create(application=application)
        # Generate PDF or other document here
        messages.success(request, 'Bursary issued and document generated.')
        return redirect('bus:application_status', application_id=application.id)
    return redirect('bus:list_bursaries')


#  Application view
@login_required
def application_detail(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'bursary/application_detail.html', {'application': application})

