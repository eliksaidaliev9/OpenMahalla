from rest_framework import serializers
from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = '__all__'
        read_only_fields = ('user', 'status', 'answer', 'answered_at')

class AppealAnswerSerializer(serializers.ModelSerializer):
    answer = serializers.CharField()