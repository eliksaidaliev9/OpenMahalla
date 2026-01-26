from rest_framework import serializers
from .models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['id', 'mahalla', 'category', 'description']
        read_only_fields = ['user', 'status', 'answer', 'created_at', 'answered_at']

    def get_answer(self, obj):
        if obj.status == Appeal.Status.ANSWERED:
            return obj.answer
        return

class AppealAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['answer']

class AppealListSerializer(serializers.ModelSerializer):
    mahalla = serializers.SlugRelatedField(slug_field='title', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    user = serializers.SlugRelatedField(slug_field=)

    class Meta:
        model = Appeal
        fields = '__all__'