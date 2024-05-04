from django.contrib import admin

from .models import BlogPost


class BlogPostAdminConfig(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(BlogPost, BlogPostAdminConfig)

