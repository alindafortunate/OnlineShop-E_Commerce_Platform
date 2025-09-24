from django.urls import path
from .views import product_list

app_name = "shop"

urlpatterns = [
    path("products/<slug:category_slug>/", product_list, name="list"),
]
