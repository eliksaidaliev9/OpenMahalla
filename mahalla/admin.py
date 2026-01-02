from django.contrib import admin
from .models import Mahalla


@admin.register(Mahalla)
class MahallaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'district')
    search_fields = ('name', 'district')
