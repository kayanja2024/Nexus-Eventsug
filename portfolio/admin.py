from django.contrib import admin

from .models import GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "media_type", "is_featured", "created_at")
    list_filter = ("category", "media_type", "is_featured")
    search_fields = ("title", "description")

# Register your models here.
