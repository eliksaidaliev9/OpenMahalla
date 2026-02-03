from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Appeal
from .serializers import AppealSerializer, AppealAnswerSerializer, AppealListSerializer
from .services import mark_under_review, mark_answered
from users.permissions import IsStaffOrAdmin, IsOwnerAndEditable


class AppealViewSet(ModelViewSet):
    # Default queryset for all appeal objects
    queryset = Appeal.objects.all()

# Setting permissions for each action
    def get_permissions(self):
        # "Answer" and "Under_Review" actions are only available to staff and admin
        if self.action in ['answer', 'under_review']:
            return [IsStaffOrAdmin()]
# Update, partial_update and delete are only available to the user with their own request and an authenticated user
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerAndEditable()]
        # require only authentication for other actions
        return [IsAuthenticated()]

# Choosing a serializer for each action
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AppealListSerializer # For list and detailed view
        if self.action == 'answer':
            return AppealAnswerSerializer # Separate serializer for response
        if self.action == 'under_review':
            return None # No serializer required
        return AppealSerializer # For default create/update

# Filtering a queryset by user
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            # Staff or admin sees all requests
            return Appeal.objects.all()
        # A simple user only sees their own references
        return Appeal.objects.filter(user=user)

# Add user to serializer in Create action
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Custom action: Move the request to "Under Review"
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsStaffOrAdmin], # Only staff/admin
        url_path='under-review', # URL: /appeals/<id>/under-review/
    )
    def under_review(self, request, pk=None):
    # Get_object() is a ModelViewSet method that retrieves the corresponding Appeal object
    # from the database using the pk (primary key) in the URL.
    # If the object is not found, it automatically returns a 404
        appeal = self.get_object()

        # The applicant can only change the application in the NEW status
        if appeal.status != Appeal.Status.NEW:
            return Response (
                {"detail": "Bu murojaat ko'rib chiqilmoqda yoki javob berilgan"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # change status to Under Review
        mark_under_review(appeal)

        return Response(
            {"detail": "Murojaat 'Under review' holatiga o'tkazildi"},
            status=status.HTTP_200_OK
        )

    # Customizing the retrieve action
    def retrieve(self, request, *args, **kwargs):
        # Get the corresponding Appeal object by pk in the URL using get_object()
        # If the object is not found, DRF automatically returns a 404
        appeal = self.get_object()
        # Convert the received object to JSON format using a serializer
        # get_serializer() – chooses the correct serializer based on get_serializer_class()
        serializer = self.get_serializer(appeal)
        # Return JSON data via Response
        return Response(serializer.data)

    # Custom action: Reply to request
    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsStaffOrAdmin], # Only staff/admin
        serializer_class=AppealAnswerSerializer
    )
    def answer(self, request, pk=None):
        appeal = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # Validation check
        mark_answered(appeal, serializer.validated_data['answer']) # Save answer

        return Response({"detail": "Javob berildi."})