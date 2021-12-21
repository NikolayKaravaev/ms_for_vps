from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from .models import Category,Inventory,Tag,Images,Storage_list

# Register your models here.
from . import models
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name","slug")
    list_display_links = ("name",)

class InvImagesInline(admin.TabularInline):
    model = Images
    extra=1
    readonly_fields = ("get_image_inv",)
    
    def get_image_inv (self,obj):
        return mark_safe(f'<img src={obj.image.url} widht="150" height="150"')
    get_image_inv.short_description = "Фото позиций"


@admin.register(Inventory)
class InventoryAdmin (admin.ModelAdmin):
    list_display = ("id","name","category","status","quality","units",)
    list_display_links = ("name",)
    list_filter=("category","storage",)
    search_fields=("name","status","category__name",)
    inlines=[InvImagesInline]
    save_on_top = True
    save_as= False
    list_editable = ("category","status","quality","units",)
    fieldsets=(
        (None,{
            "fields":(("name","status","tags","category"),)
        }),
        (None,{
            "fields":(("storage","stellage","shelf"),)
        }),
        (None,{
            "fields":(("quality","units"),)
        }),
    )


@admin.register(Storage_list)
class Storage_listAdmin (admin.ModelAdmin):
    list_display = ("id","name","slug","address","get_image_storage","get_image_key")
    readonly_fields=("get_image_storage","get_image_key")
    list_display_links = ("name",)

    def get_image_storage (self,obj):
        return mark_safe(f'<img src={obj.storage_photo.url} widht="150" height="150"')

    get_image_storage.short_description = "Фото гаража"
   
    def get_image_key (self,obj):
        return mark_safe(f'<img src={obj.keys_photo.url} widht="150" height="150"')

    get_image_key.short_description = "Фото ключей"

@admin.register(Tag)
class TagAdmin (admin.ModelAdmin):
    list_display = ("id","name","slug")
    list_display_links = ("name",)

@admin.register(Images)
class ImagesAdmin (admin.ModelAdmin):
    list_display = ("id","get_image_inv")
    readonly_fields=("get_image_inv",)
    list_display_links = ("id",)
    def get_image_inv (self,obj):
        return mark_safe(f'<img src={obj.image.url} widht="150" height="150"')

    get_image_inv.short_description = "Фото позиций"

class ImagesInLine(admin.StackedInline):
    model=models.Images
    extra=1

