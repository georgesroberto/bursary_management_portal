from django.urls import path
from . import views

app_name = 'bus'

urlpatterns = [
    # Dashboard
    path('', views.bursary_list, name='index'),

    # Bursary
    path('list/', views.bursary_list, name='list_bursaries'),
    path('create/', views.create_bursary, name='create_bursary'),
    path('<int:bursary_id>/update/', views.update_bursary, name='update_bursary'),
    path('<int:bursary_id>/delete/', views.delete_bursary, name='delete_bursary'),

    # Questionnaire and Applications
    path('<int:bursary_id>/questionnaire/', views.create_questionnaire, name='create_questionnaire'),
    path('<int:bursary_id>/apply/', views.submit_application, name='submit_application'),
    path('application/<int:application_id>/issue/', views.issue_bursary, name='issue_bursary'),
]

