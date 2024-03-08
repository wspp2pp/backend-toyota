from django.urls import path

from .views import ListCategoriesView

app_name = "product"
urlpatterns = [
    path('all/', ListCategoriesView.as_view())
]
