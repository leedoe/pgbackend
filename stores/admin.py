from stores.models import Store
from django.contrib import admin


# Register your models here.
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
