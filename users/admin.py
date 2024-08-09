from django.contrib import admin
from .models import Person

@admin.register(Person)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'status', 'is_staff', 'is_active')
    list_filter = ('status', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'status')
