from rest_framework import viewsets, filters
from users.permissions import IsStaffOrReadOnly
from .models import Mahalla
from .serializers import MahallaSerializer


class MahallaViewSet(viewsets.ModelViewSet):
    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer
    permission_classes = [IsStaffOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'district']

