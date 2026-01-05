from logging import raiseExceptions

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Appeal
from .serializers import AppealSerializer, AppealAnswerSerializer
from .services import mark_answered, mark_under_review
from users.permissions import IsStaffOrReadOnly, IsOwnerOrReadOnly


class AppealViewSet(ModelViewSet):
    serializer_class = AppealSerializer
    permission_classes = IsOwnerOrReadOnly

    def get_queryset(self):
        user = self.queryset.user
        if user.is_staff:
            return Appeal.objects.all()
        return Appeal.objects.filter(user=user)

    def perform_create(self, serializer):
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