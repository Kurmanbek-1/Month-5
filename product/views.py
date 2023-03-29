from rest_framework.decorators import api_view
from product.models import Category, Product, Review
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, ReviewSerializer


@api_view(['GET'])
def list_Product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=False)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
