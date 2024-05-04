from django.contrib import admin

from .models import LookBook, LookBookImage


class LookBookImageInline(admin.StackedInline):
    model = LookBookImage


class LookBookAdminConfig(admin.ModelAdmin):
    list_display = ['title']
    inlines = [LookBookImageInline]


admin.site.register(LookBook, LookBookAdminConfig)

