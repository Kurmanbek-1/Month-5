from rest_framework.decorators import api_view
from product.models import Category, Product, Review
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, ReviewSerializer
from rest_framework import status


@api_view(['GET'])
def list_Product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Product_detail(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    serializer = ProductSerializer(products)
    return Response(data=serializer.data)

@api_view(['GET'])
def list_Category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=False)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Category_detail(request, id):
    try:
        categories = Product.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    serializer = CategorySerializer(categories)
    return Response(data=serializer.data)


@api_view(['GET'])
def list_Review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

@api_view(['GET'])
def list_Review_detail(request, id):
    try:
        reviews = Product.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    serializer = ReviewSerializer(reviews)
    return Response(data=serializer.data)