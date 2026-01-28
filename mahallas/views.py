from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Mahalla
from .serializers import MahallaSerializer

# ViewSet for the Mahalla model
class MahallaViewSet(viewsets.ModelViewSet):
    # ModelViewSet provides automatic CRUD operations: list, retrieve, create, update, destroy

    queryset = Mahalla.objects.all()  # Queryset for mahalla list
    serializer_class = MahallaSerializer # Serializer that converts the Mahalla model to JSON format

    # SearchFilter allows you to search by 'title' and 'district' in the admin panel and API
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'district']

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()] # only list authenticated users
        return [IsAdmin()]  # all other actions are admin only
