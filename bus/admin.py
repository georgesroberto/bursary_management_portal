from django.contrib import admin
from .models import Bursary,Application, Document

@admin.register(Bursary)
class BursaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'posted_by')
    search_fields = ('title', 'description')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'bursary', 'status')
    list_filter = ('status',)
    search_fields = ('student__first_name', 'student__last_name', 'bursary__title')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('application', 'file')
    search_fields = ('application__student__first_name', 'application__student__last_name', 'application__bursary__title')


admin.site.site_header = 'Bursary Management System'
admin.site.site_title = 'Bursary Management System'
