from django.contrib import admin

from .models import Category


class CategoryAdminConfig(admin.ModelAdmin):
    list_display = ['title', 'parent']


admin.site.register(Category, CategoryAdminConfig)

