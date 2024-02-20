from rest_framework import serializers
from .models import Concert, Category


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ('title', 'cat_id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'