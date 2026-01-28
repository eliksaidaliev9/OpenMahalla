from rest_framework import serializers
from .models import User

# Serializer for user registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # Which model do work with
        fields = ['id', 'phone_number', 'username', 'password'] # fields visible to the user
        # password is for write-only (will not appear in API response)
        extra_kwargs = {'password': {'write_only': True}}
        ref_name = "OpenMahallaUser"  # To avoid name collision in Swagger/drf-spectacular

# Custom create method
    def create(self, validated_data):
        # Will remove the password separately
        password = validated_data.pop('password')
        # Create a user using create_user
        # role will always be 'applicant' (simple user)
        return User.objects.create_user(
            role='applicant',
            password=password,
            **validated_data
        )
