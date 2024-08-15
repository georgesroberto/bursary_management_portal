from django.shortcuts import render
from bus.models import Bursary

def index(request):
    bursaries = Bursary.objects.all()
    context = {'bursaries':bursaries}
    return render(request, 'main_app/index.html', context)

def about(request):
    return render(request, 'main_app/about.html')

def contact(request):
    return render(request, 'main_app/contact.html')

def permission_denied_view(request):
    return render(request, 'main_app/403.html', status=403)