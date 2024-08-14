from django.urls import path
from . import views

app_name = 'std'

urlpatterns = [
    path('', views.application_index, name='index'),

    # Student URLS
    path('list/', views.student_list, name='student_list'),
    
    # Application
    path('bursaries/', views.view_bursaries, name='view_bursaries'),
    path('bursary/<int:bursary_id>/apply/', views.apply_for_bursary, name='apply_for_bursary'),

    # Others
    path('applications/', views.view_application_status, name='application_status'),
]

