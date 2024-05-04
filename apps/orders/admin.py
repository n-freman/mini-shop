from django.contrib import admin

from .models import Order, OrderProduct


class OrderProductAdmin(admin.StackedInline):
    model = OrderProduct


class OrderAdminConfig(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'client_phone']
    inlines = [OrderProductAdmin]


admin.site.register(Order, OrderAdminConfig)

