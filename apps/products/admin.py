from django.contrib import admin

from .models import (
    Product,
    ProductImage,
    ProductColor,
    ProductSize
)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 0


class ProductColorInline(admin.StackedInline):
    model = ProductColor
    extra = 0


class ProductSizeInline(admin.StackedInline):
    model = ProductSize
    extra = 0


class ProductAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [ProductImageInline, ProductColorInline, ProductSizeInline]


admin.site.register(Product, ProductAdminConfig)

