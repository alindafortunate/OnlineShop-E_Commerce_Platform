from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
import csv
import datetime
from django.http import HttpResponse


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ""


order_payment.short_description = "Stripe payment"


def export_data_to_csv(modeladmin, request, queryset):
    """This functions export data from the django admin to a csv file."""
    opts = modeladmin.model._meta
    response = HttpResponse(
        content_type="text/csv",
        headers={
            "Content-Disposition": f'attachment; filename="{opts.verbose_name}.csv"'
        },
    )

    csv_writer = csv.writer(response)
    fields = [
        field
        for field in opts.get_fields()
        if not field.many_to_many and not field.one_to_many
    ]
    # Write the first data row (That's the heading)
    csv_writer.writerow([field.verbose_name for field in fields])

    # Writing the values for the field names.
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        csv_writer.writerow(data_row)

    return response


export_data_to_csv.short_description = "Export to CSV"


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        order_payment,
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
    actions = [export_data_to_csv]
