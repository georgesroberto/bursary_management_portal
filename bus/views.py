# Import statements

from core.decorators import check_group_permission
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

from .models import Application, Document, Bursary
from .forms import BursaryForm

# Create your views here.
# @check_group_permission(['Checklist', 'Administrator'])
def bursary_index(request):
    bursaries = Bursary.objects.all()
    applications = Application.objects.all()
    return render(request, 'bursary/index.html', {'bursaries':bursaries,'applications':applications})

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


@login_required
def issue_bursary(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if application.status == 'Submitted':
        # Create a buffer for the PDF
        buffer = BytesIO()
        pdf = SimpleDocTemplate(
            buffer,
            pagesize=letter,
            rightMargin=2 * inch,
            leftMargin=2 * inch,
            topMargin=2 * inch,
            bottomMargin=2 * inch
        )

        # Create styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="Justified", alignment=TA_JUSTIFY, fontName="Helvetica", fontSize=12))
        styles.add(ParagraphStyle(name="CenteredBold", alignment=TA_CENTER, fontName="Helvetica-Bold", fontSize=12))

        # Content paragraphs
        content = [
            Paragraph(f"{application.bursary.posted_by},", styles["Justified"]),
            Paragraph(f"{application.bursary.posted_by.username},", styles["Justified"]),
            Paragraph(f"{application.bursary.posted_by.status} Office,<br/>Address", styles["Justified"]),
            Spacer(1, 12),  
            Paragraph(f"{application.student.institution.name},<br/>{application.student.institution.address},", styles["Justified"]),
            Spacer(1, 12),
            Paragraph(f"DATE: {timezone.now().date()}", styles["Justified"]),
            Spacer(1, 12),
            Paragraph(f"<b>RE: APPROVAL OF APPLIED BURSARY</b>", styles["Justified"]),
            Spacer(1, 12),
            Paragraph(
                f"We are pleased to inform you that your application for the \"{application.bursary.title}\" bursary was successful and has been approved.",
                styles["Justified"]
            ),
            Paragraph(
                f"The amount of {application.bursary.amount} has been granted to you. Kindly visit the County CDF office to pick up your cheque addressed to {application.student.institution.name}. "
                "Please carry along a letter from the institution when coming to collect your cheque.",
                styles["Justified"]
            ),
            Paragraph(
                f"The reference number for your bursary is: {application.student.student_id} for verification.",
                styles["Justified"]
            ),
            Spacer(1, 12),
            Paragraph("Regards,", styles["Justified"]),
            Paragraph(f"{application.bursary.posted_by.username},<br/>CDF Officer", styles["Justified"]),
            Spacer(1, 24),
            Paragraph(
                "<b>BursaryMS</b><br/><a href='http://yourwebsite.com'>Visit our website</a>",
                styles["CenteredBold"]
            )
        ]

        # Build the PDF
        pdf.build(content)

        # Get the PDF data and attach it to the application
        buffer.seek(0)
        document = Document.objects.create(application=application)
        document.file.save(f'bursary_{application.student.student_id}.pdf', buffer, save=True)

        # Close the buffer
        buffer.close()

        # Change the application status to 'Approved'
        application.status = 'Approved'
        application.save()

        messages.success(request, 'Bursary approved and document generated.')
        return redirect('bus:application_completed', application_id=application.id)
    
    messages.error(request, 'Bursary cannot be issued. Invalid application status.')
    return redirect('bus:application_pending')


@login_required
def reject_bursary(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    if application.status == 'Submitted':
        application.status = 'Rejected'
        application.save()

        messages.success(request, 'Bursary application rejected.')
        return redirect('bus:list_bursaries')

    messages.error(request, 'Bursary cannot be accepted. Invalid application status.')
    return redirect('bus:list_bursaries')


#  Application view
def application_list(request):
    applications = Application.objects.all()
    return render(request, 'bursary/application_list.html', {'applications':applications})

def application_pending(request):
    applications = Application.objects.all().filter(status='Submitted')
    return render(request, 'bursary/application_pending.html', {'applications':applications})

@login_required
def application_detail(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    return render(request, 'bursary/application_detail.html', {'application': application})

