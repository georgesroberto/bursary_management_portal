from django.shortcuts import render
from django.http import HttpResponse
from core.decorators import check_group_permission

# Create your views here.
@check_group_permission(['Checklist', 'Administrator'])
def index(request):
    return HttpResponse('Home')