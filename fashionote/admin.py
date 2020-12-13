from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'tag_list')
    list_display_links = ('id', 'brand_name')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
