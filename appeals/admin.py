from django.contrib import admin
from .models import Appeal

# Registering the Appeal model in the Django admin panel
@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    # Columns displayed in list view in admin panel
    list_display = ('id', 'full_name', 'user', 'mahalla', 'category', 'status', 'created_at')
    # Columns for filter panel
    # In the admin panel, the user can filter by these columns
    list_filter = ('status', 'mahalla', 'category', 'created_at')
    # Columns for the search bar
    # In the admin panel, the user can search on these columns
    # Added the username field in the user model to the search with 'user__username'
    search_fields = ('description', 'user__username')
