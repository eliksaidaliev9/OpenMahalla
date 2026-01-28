from rest_framework import serializers
from .models import Appeal

# Serializer to create/view user reference
class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        # These are the fields that the user can view and create through the serializer
        fields = ['id', 'full_name', 'mahalla', 'category', 'description']
        # The following fields are read-only, the user cannot submit them.
        read_only_fields = ['user', 'status', 'answer', 'created_at', 'answered_at']
    # The answer is only displayed if the status is "ANSWERED".
    def get_answer(self, obj):
        if obj.status == Appeal.Status.ANSWERED:
            return obj.answer
        return # If no response is given, it returns nothing

# Serializer for responding to admin or staff requests
class AppealAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ['answer'] # Only works with the 'answer' field

# Serializer to display a list of references
class AppealListSerializer(serializers.ModelSerializer):
    # Show title for Mahalla and Category fields via slug_field
    mahalla = serializers.SlugRelatedField(slug_field='title', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Appeal
        fields = '__all__' # All fields are visible in the list
