from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer
from users.permissions import IsStaffOrAdmin


class CategoryViewSet(ModelViewSet):
    # Default queryset — all categories
    queryset = Category.objects.all()
    # Serializer — Adapts the Category model to the API
    serializer_class = CategorySerializer

# Filtering a queryset by user
    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            # Staff and admin see all categories
            return Category.objects.all()
        # A simple user only sees active categories
        return Category.objects.filter(is_active=True)

# Permissions for each action
    def get_permissions(self):
        if self.action == 'list':
            # Only authenticated users can view the list
            return [IsAuthenticated()]
        # Other actions (create, update, delete) are only available to staff/admin.
        return [IsStaffOrAdmin()]
