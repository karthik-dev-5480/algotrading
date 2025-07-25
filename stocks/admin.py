# stocks/admin.py
from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol',)  # Only 'symbol' since 'name' doesn't exist
    search_fields = ('symbol',)