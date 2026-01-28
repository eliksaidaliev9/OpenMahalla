from django.contrib import admin
from .models import User

# Registering the User model in the admin panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Columns visible in the admin list
    list_display = ('id', 'username', 'phone_number', 'role', 'is_active', 'is_staff', 'is_superuser')
    # Columns for filter panel
    list_filter = ('role', 'is_staff', 'is_superuser')
    # Columns for the search bar
    search_fields = ('username', 'phone_number')

# Automatically set is_staff and is_superuser based on role when user is saved
    def save_model(self, request, obj, form, change):
        # If the role is 'admin', the user will be staff and superuser
        if obj.role == 'admin':
            obj.is_staff = True
            obj.is_superuser = True
        # If role is 'staff', staff but not superuser
        elif obj.role == 'staff':
            obj.is_staff = True
            obj.is_superuser = False
        # There will be no other roles (applicant) staff and superuser.
        else:
            obj.is_staff = False
            obj.is_superuser = False

        super().save_model(request, obj, form, change) # Default save_model call
