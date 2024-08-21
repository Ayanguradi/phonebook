from django.contrib import admin
from .models import Shop, Subcategory,Category, ShopImage,CarouselImage 

# Register your models here.

# class CategoryImageInline(admin.TabularInline):
#     model = CategoryImage
#     extra = 1

class ShopImageInline(admin.TabularInline):
    model = ShopImage
    extra = 1

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     inlines = [CategoryImageInline]

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [ShopImageInline]

class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_text', 'order')
    list_editable = ('alt_text', 'order')

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(CarouselImage)
