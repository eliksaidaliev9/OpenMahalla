from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Appeal
from .serializers import AppealSerializer, AppealAnswerSerializer
from .services import mark_answered, mark_under_review
from users.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly


class AppealViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Appeal.objects.none()
        user = getattr(self.request, 'user', None)
        if not user or user.is_anonymous:
            return Appeal.objects.none()

        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Appeal.objects.all()
        return Appeal.objects.filter(user=user)

    def perform_create(self, serializer):
        if getattr(self, 'swagger_fake_view', False):
            return
        user = getattr(self.request, 'user', None)
        if not user or user.is_anonymous:
            return
        serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'], permission_classes=[IsStaffOrReadOnly])
    def under_review(self, request, pk=None):
        appeal = self.get_object()
        mark_under_review(appeal)
        return Response({"detail": "Ko'rib chiqilyapti."})

    @action(
        detail=True,
        methods=['post'],
        permission_classes=[IsStaffOrReadOnly],
        serializer_class=AppealAnswerSerializer)
    def answer(self, request, pk=None):
        appeal = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mark_answered(appeal, serializer.validated_data['answer'])
        return Response({"detail": "Javob berildi."})