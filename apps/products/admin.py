from django.contrib import admin

from .models import (
    Product,
    ProductImage,
    ProductColor,
    ProductSize
)


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductColorInline(admin.StackedInline):
    model = ProductColor


class ProductSizeInline(admin.StackedInline):
    model = ProductSize


class ProductAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [ProductImageInline, ProductColorInline, ProductSizeInline]


admin.site.register(Product, ProductAdminConfig)

