from django.contrib import admin
from .models import Booking, Category

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Booking, BookingAdmin)
admin.site.register(Category, CategoryAdmin)
