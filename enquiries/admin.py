from django.contrib import admin
from .models import EnquiryMessage


@admin.register(EnquiryMessage)
class EnquiryMessageAdmin(admin.ModelAdmin):
    """
    Admin options for the Enquiry model.
    """
    list_display = ('date_created', 'topic', 'email', 'message')
    ordering = ('-date_created',)