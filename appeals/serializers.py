from rest_framework import serializers
from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'mahalla', 'category', 'description']
        read_only_fields = ['user', 'status', 'answer', 'answered_at']

class AppealAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['answer']