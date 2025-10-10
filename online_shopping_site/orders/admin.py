from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "address", "city"]
    list_filter = ["created", "paid", "updated"]
    inlines = [OrderItemInline]
