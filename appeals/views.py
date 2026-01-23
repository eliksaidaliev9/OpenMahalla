from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Appeal
from .serializers import AppealSerializer, AppealAnswerSerializer
from users.permissions import IsStaffOrAdmin, IsOwnerAndEditable


class AppealViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerAndEditable]
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Appeal.objects.all()
        return Appeal.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        appeal = self.get_object()

        if request.user.is_staff and appeal.status == Appeal.Status.NEW:
            appeal.mark_under_review()

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
        appeal.mark_answered(serializer.validated_data['answer'])

        return Response({"detail": "Javob berildi."})