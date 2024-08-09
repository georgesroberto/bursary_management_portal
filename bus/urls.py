from django.urls import path
from . import views

app_name = 'bus'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_bursary, name='create_bursary'),
    path('<int:bursary_id>/questionnaire/', views.create_questionnaire, name='create_questionnaire'),
    path('<int:bursary_id>/apply/', views.submit_application, name='submit_application'),
    path('application/<int:application_id>/issue/', views.issue_bursary, name='issue_bursary'),
]

