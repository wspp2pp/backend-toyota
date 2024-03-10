from django.urls import path

from .views import list_product_by_category

app_name = "product"
urlpatterns = [
    path('by-category/<category_id>/', list_product_by_category, name='list_product_by_category')
]
