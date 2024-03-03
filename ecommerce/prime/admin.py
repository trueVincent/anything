from django.contrib import admin
from prime.models import Product, Category, Order, OrderItem, Address


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Product, BaseAdmin)
admin.site.register(Category, BaseAdmin)
admin.site.register(Order, BaseAdmin)
admin.site.register(OrderItem, BaseAdmin)
admin.site.register(Address, BaseAdmin)
