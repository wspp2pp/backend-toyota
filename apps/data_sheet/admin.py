# admin.py

from django.contrib import admin
from .models import DataSheet
from .forms import DataSheetAdminForm


class DataSheetAdmin(admin.ModelAdmin):
    form = DataSheetAdminForm

    list_display = ('title', 'subtitle', 'principal', 'product_name')
    list_filter = ('principal', 'product__name')
    search_fields = ('title', 'subtitle', 'description')
    list_per_page = 20

    @staticmethod
    def product_name(obj):
        return obj.product.name


admin.site.register(DataSheet, DataSheetAdmin)
