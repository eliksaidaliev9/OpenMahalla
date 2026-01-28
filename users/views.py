from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin

# The main ViewSet for the User model
class UserViewSet(viewsets.ModelViewSet):
    # ModelViewSet automatically provides CRUD (list, retrieve, create, update, delete) operations for users
    queryset = User.objects.all()  # Queryset for user list
    serializer_class = UserSerializer # Serializer that converts the User model to JSON format

 # Dynamic permission management
    def get_permissions(self):
        # create (register) everyone allowed
        if self.action == 'create':
            return [AllowAny()]
        # all other actions are admin only
        return [IsAdmin()]

  # Create a user (registration)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # data verification
        serializer.save()  # Save to database
        return Response(serializer.data, status=status.HTTP_201_CREATED)