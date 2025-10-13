from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("order/", views.order_create, name="orders"),
]
