from rest_framework import serializers
from .models import Category

# Serializing the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category # Which model do work with
        fields = ['id', 'title'] # fields visible to the user
