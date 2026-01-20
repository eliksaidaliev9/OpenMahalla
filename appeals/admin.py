from django.contrib import admin
from .models import Appeal, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'mahalla', 'category', 'status', 'created_at')
    list_filter = ('status', 'mahalla', 'category', 'created_at')
    search_fields = ('title', 'description', 'user__username')
