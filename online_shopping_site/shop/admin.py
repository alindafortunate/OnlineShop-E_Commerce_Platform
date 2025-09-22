from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}
# On this day I posed to first take off a break off the screen for more than 24 hours.
# From 22/9/2025 at 3:51 pm to 24/9/2025 in the morning hours.