from django.urls import path

from .views import list_categories

app_name = "category"
urlpatterns = [
    path('all/', list_categories)
]
