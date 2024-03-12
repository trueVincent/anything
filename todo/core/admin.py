from django.contrib import admin

from core.models import Todo


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Todo, BaseAdmin)
