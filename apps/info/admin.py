from django.contrib import admin
from .models import Info


class InfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'section')
    list_display_links = ('name',)
    search_fields = ('name', 'section')
    list_filter = ('name', 'url', 'section')
    list_per_page = 25


admin.site.register(Info, InfoAdmin)
