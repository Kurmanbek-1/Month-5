from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import UserLoginvalidateSerialzer, UserCreateValidateSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserLoginvalidateSerialzer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(serializer.validated_data)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'Ошибка': 'Username и password не правильны!'})

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})

