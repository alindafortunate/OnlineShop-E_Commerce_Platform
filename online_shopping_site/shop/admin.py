from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.contrib.admin import ModelAdmin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ["name", "slug"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


# On this day I posed to first take off a break off the screen for more than 24 hours.
# From 22/9/2025 at 3:51 pm to 24/9/2025 in the morning hours.
