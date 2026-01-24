from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer
from users.permissions import IsStaffOrAdmin


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Category.objects.all()
        return Category.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsStaffOrAdmin()]
