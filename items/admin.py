from items.models import Comment
from utils.s3.s3 import upload_file
from items.forms import MaterialAdminForm, TanneryAdminForm
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

@admin.register(Comment)
@admin.register(LeatherDetail)
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = MaterialAdminForm

    def save_model(self, request, obj, form, change):
        try:
            print(request.FILES)
            url = upload_file(request.FILES['imageFile'].file)
            obj.image = url
        except KeyError as e:
            pass
        return super().save_model(request, obj, form, change)

@admin.register(Tannery)
class TanneryAdmin(admin.ModelAdmin):
    form = TanneryAdminForm

    def save_model(self, request, obj, form, change):
        try:
            url = upload_file(request.FILES['imageFile'].file)
            obj.logo = url
        except KeyError as e:
            pass
        return super().save_model(request, obj, form, change)