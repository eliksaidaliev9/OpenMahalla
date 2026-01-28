from django.contrib import admin
from .models import Mahalla


@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'district')  # Columns visible in the admin panel
    search_fields = ('title', 'district')  # Search fields
