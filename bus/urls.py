from django.urls import path
from . import views

app_name = 'bus'

urlpatterns = [
    # Dashboard
    path('', views.bursary_index, name='index'),

    # Bursary
    path('list/', views.bursary_list, name='list_bursaries'),
    path('create/', views.create_bursary, name='create_bursary'),
    path('<int:bursary_id>/update/', views.update_bursary, name='update_bursary'),
    path('<int:bursary_id>/delete/', views.delete_bursary, name='delete_bursary'),

    # Applications
    path('applications/completed/', views.application_list, name='application_list'),
    path('applications/pending/', views.application_pending, name='application_pending'),
    path('application/<int:application_id>/issue/', views.issue_bursary, name='issue_bursary'),
    path('application/<int:application_id>/reject/', views.reject_bursary, name='reject_bursary'),
]

