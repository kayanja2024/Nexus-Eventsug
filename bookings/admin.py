from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "event_type", "event_date", "status", "created_at")
    list_filter = ("status", "event_type")
    search_fields = ("full_name", "email", "phone", "location")

# Register your models here.
