from django.urls import path
from .views import *

app_name = 'bus'

urlpatterns = [
    path('', index, name='index')
]