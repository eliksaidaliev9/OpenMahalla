from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer
from users.permissions import IsStaffOrAdmin


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Category.objects.all()
        return Category.objects.filter(is_active=True)
