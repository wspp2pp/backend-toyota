from django.urls import path

from .views import list_data_sheet_by_product

app_name = "data_sheet"
urlpatterns = [
    path('by-product/<product_id>', list_data_sheet_by_product)
]
