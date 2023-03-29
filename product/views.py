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
def list_Product_detail(request):
    products = Product.objects.all(id=id)
    serializer = ProductSerializer(products)
    return Response(data=serializer.data)

@api_view(['GET'])
def list_Category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=False)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Category_detail(request):
    categories = Product.objects.all(id=id)
    serializer = CategorySerializer(categories)
    return Response(data=serializer.data)


@api_view(['GET'])
def list_Review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Review_detail(request):
    reviews = Product.objects.all(id=id)
    serializer = ReviewSerializer(reviews)
    return Response(data=serializer.data)