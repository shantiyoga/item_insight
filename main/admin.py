from django.contrib import admin
from main.models import ItemStore

# Register your models here.
@admin.register(ItemStore)

class ItemStore(admin.ModelAdmin):
    list_display = ['name', 'amount', 'price', 'category', 'description']
    list_filter = ['description']