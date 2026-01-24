from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Mahalla
from .serializers import MahallaSerializer


class MahallaViewSet(viewsets.ModelViewSet):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'district']

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return [IsAdmin()]
