from django.urls import path

from .views import ListProductByCategoryView

app_name = "product"
urlpatterns = [
    path('by-category/<category_id>', ListProductByCategoryView.as_view())
]
