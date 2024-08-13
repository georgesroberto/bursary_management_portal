from django.urls import path
from . import views

app_name = 'std'

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register_student, name='register_student'),
    path('bursaries/', views.view_bursaries, name='view_bursaries'),
    path('bursary/<int:bursary_id>/apply/', views.apply_for_bursary, name='apply_for_bursary'),
    path('applications/', views.view_application_status, name='application_status'),
]

