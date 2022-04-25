from django.contrib import admin
from .models import Service, Category

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    """Admin model for services."""
    list_display = (
        "name",
        "blurb",
        "genre",
        "price",
        "image",
    )
    ordering = ("name",)


class CategoryAdmin(admin.ModelAdmin):
    """Admin model for Category"""
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Service)
admin.site.register(Category)
