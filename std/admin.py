from django.contrib import admin
from .models import Institution, Student

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_person')
    search_fields = ('name', 'contact_person__username')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'first_name', 'last_name', 'email', 'institution')
    search_fields = ('registration_number', 'first_name', 'last_name', 'institution__name')
