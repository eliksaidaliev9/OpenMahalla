from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

