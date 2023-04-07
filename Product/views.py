from rest_framework.decorators import api_view
from Product.models import Category, Product, Review
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, ReviewSerializer, ReviewProductSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def list_Product(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        # review = request.data.get('review')
        product = Product.objects.create(title=title, description=description,
                                         price=price, category_id=category_id)
        # product.reviews.set(review)
        product.save()
        return Response(data=ProductSerializer(product).data)



@api_view(['GET', 'PUT', 'DELETE'])
def list_Product_detail(request, id):
    try:
        products = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    if request.method == 'GET':
        serializer = ProductSerializer(products)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        products.title = request.data.get('title')
        products.description = request.data.get('description')
        products.price = request.data.get('price')
        products.category_id = request.data.get('category_id')
        # reviews = request.data.get('reviews')
        # products.reviews.set(reviews)
        products.save()
        return Response(data=ProductSerializer(products).data)


@api_view(['GET', 'POST'])
def list_Category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)



@api_view(['GET', 'PUT', 'DELETE'])
def list_Category_detail(request, id):
    try:
        categories = Product.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    if request.method == 'GET':
        serializer = CategorySerializer(categories)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        categories.name = request.data.get('name')
        categories.save()
        return Response(data=CategorySerializer(categories).data)


@api_view(['GET', 'POST'])
def list_Review(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
        text = request.data.get('text')
        reviews = Review.objects.create(product_id=product_id, stars=stars,
                                        text=text)
        return Response(data=ReviewSerializer(reviews).data)




@api_view(['GET', 'PUT', 'DELETE'])
def list_Review_detail(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'Ошибка': 'Этот объект не найдет!'})
    if request.method == 'GET':
        serializer = ReviewSerializer(reviews, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        Review.product_id = request.data.get('product_id')
        Review.stars = request.data.get('stars')
        Review.text = request.data.get('text')
        reviews.save()
        return Response(data=ReviewSerializer(reviews).data)
    elif request.method == 'DELETE':
        list_Review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_reviews(request):
    products = Product.objects.all()
    serializer = ReviewProductSerializer(products, many=True)
    return Response(data=serializer.data)
