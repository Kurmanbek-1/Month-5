from django.db.models import Avg
from rest_framework import serializers
from .models import Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product_id'.split()

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = 'id title price description category_name reviews'.split()


class CategorySerializer(serializers.ModelSerializer):
    product_count = ProductSerializer
    class Meta:
        model = Category
        fields = 'name product_count'.split()



class ReviewProductSerializer(serializers.Serializer):
    average_rating = serializers.SerializerMethodField()
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=150)
    reviews = ReviewSerializer(many=True)

    def get_average_rating(self, obj):
        return round(obj.reviews.aggregate(avg_rating=Avg('stars'))['avg_rating'], 2)
