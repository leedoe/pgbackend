from django.contrib import admin

from items.models import Item, Leather, LeatherDetail, Material, Tannery

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "store_name"]
    search_fields = ["name"]

@admin.register(Leather)
class LeatherAdmin(admin.ModelAdmin):
    list_display = ['name', 'material']
    pass

@admin.register(LeatherDetail)
@admin.register(Material)

@admin.register(Tannery)
class TanneryAdmin(admin.ModelAdmin):
    pass
