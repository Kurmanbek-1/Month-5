from rest_framework import serializers
from .models import Category, Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product'

