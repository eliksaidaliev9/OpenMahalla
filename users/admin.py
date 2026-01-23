from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone_number', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'phone_number')

    def save_model(self, request, obj, form, change):
        if obj.role == 'is_superuser':
            obj.is_staff = True
            obj.is_superuser = True
        elif obj.role == 'is_staff':
            obj.is_staff = True
            obj.is_superuser = False
        else:
            obj.is_staff = False
            obj.is_superuser = False

        super().save_model(request, obj, form, change)
