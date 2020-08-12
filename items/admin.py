from items.models import Item
from django.contrib import admin

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "store_name"]
    search_fields = ["name"]
