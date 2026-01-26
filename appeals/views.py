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
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    def get_permissions(self):
        if self.action in ['answer', 'under_review']:
            return [IsStaffOrAdmin()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerAndEditable()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return AppealListSerializer
        return AppealSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Appeal.objects.all()
        return Appeal.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsStaffOrAdmin],
        url_path='under-review',
        serializer_class=None,
    )
    def under_review(self, request, pk=None):
        appeal = self.get_object()

        if appeal.status != Appeal.Status.NEW:
            return Response (
                {"detail": "Bu murojaat ko'rib chiqilmoqda yoki javob berilgan"},
                status=status.HTTP_400_BAD_REQUEST
            )
        mark_under_review(appeal)

        return Response(
            {"detail": "Murojaat 'Under review' holatiga o'tkazildi"},
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        appeal = self.get_object()
        serializer = self.get_serializer(appeal)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsStaffOrAdmin],
        serializer_class=AppealAnswerSerializer
    )
    def answer(self, request, pk=None):
        appeal = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mark_answered(appeal, serializer.validated_data['answer'])

        return Response({"detail": "Javob berildi."})