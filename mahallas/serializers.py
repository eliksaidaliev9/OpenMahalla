from rest_framework import serializers
from .models import Mahalla

class MahallaSerializer(serializers.ModelSerializer):
    # Serializer to read neighborhood model into JSON format
    class Meta:
        model = Mahalla  # Shows which model it works with
        fields = '__all__'  # Outputs all fields in the model to the API