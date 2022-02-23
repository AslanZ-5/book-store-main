from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin
from .models import (Category,
                     Product,
                     ProductImage,
                     ProductSecification,
                     ProductSpecificationValue,
                     ProductType,
                     )
admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(Product)
# admin.site.register(ProductImage)
# admin.site.register(ProductSecification)
# admin.site.register(ProductSpecificationValue)


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [ 
        ProductSpecificationInline
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage
class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
        

    ]

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_diplay = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name', )}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
#     prepopulated_fields = {'slug': ('title', )}
