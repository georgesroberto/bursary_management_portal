from django.urls import path
from . import views

app_name = 'std'

urlpatterns = [
    path('', views.student_index, name='index'),

    # Student URLS
    path('list/', views.student_list, name='student_list'),
    
    # Application
    path('bursaries/', views.view_bursaries, name='view_bursaries'),
    path('application/', views.application_list, name='application_list'),
    path('application/<int:bursary_id>/<int:student_id>/', views.apply_for_bursary, name='apply_for_bursary'),

    # Others
    path('applications/', views.view_application_status, name='application_status'),
]

