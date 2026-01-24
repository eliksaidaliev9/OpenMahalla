from django.contrib import admin
from .models import Appeal

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mahalla', 'category', 'status', 'created_at')
    list_filter = ('status', 'mahalla', 'category', 'created_at')
    search_fields = ('description', 'user__username')
