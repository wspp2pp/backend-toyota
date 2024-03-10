from django.urls import path

from apps.info.views import list_info

app_name = "info"
urlpatterns = [
    path('all/', list_info, name='list_info')
]
