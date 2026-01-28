from django.contrib import admin
from .models import Category

# Registering the Category model in the admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Columns visible in the list in the admin panel
    list_display = ('id', 'title', 'is_active')
    # Columns for filter panel
    list_filter = ('is_active',)
    # Columns for the search bar
    search_fields = ('title',)

