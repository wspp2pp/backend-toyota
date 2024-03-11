# admin.py

from django.contrib import admin
from .models import Product
from .forms import ProductAdminForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

    list_display = ('name', 'price', 'year', 'category_name')
    list_filter = ('price', 'year', 'category__name')
    search_fields = ('name', )
    list_per_page = 20

    @staticmethod
    def category_name(obj):
        return obj.category.name


admin.site.register(Product, ProductAdmin)
