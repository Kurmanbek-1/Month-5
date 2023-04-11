# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
from users.serializer import (UserLoginvalidateSerialzer, UserCreateValidateSerializer,
                              ConfirmUserValidateSerializer)
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
# from .models import ConfirmUser


class AuthorizationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginvalidateSerialzer


class RegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateValidateSerializer


class UserExaminationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ConfirmUserValidateSerializer

# -------------------------------------------------------------------------------------------------------------------

# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserLoginvalidateSerialzer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     print(serializer.validated_data)
#     user = authenticate(**serializer.validated_data)
#     if user:
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED,
#                     data={'Ошибка': 'Username и password не правильны!'})

# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data)
#     return Response(status=status.HTTP_201_CREATED,
#                     data={'user_id': user.id})

# @api_view(['POST'])
# def confirm_api_view(request):
#     serializer = ConfirmUserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     try:
#         if ConfirmUser.objects.filter(code=request.data['code']):
#             User.objects.update(is_active=True)
#             return Response(status=status.HTTP_200_OK,
#                             data={'Ok!': 'User is active'})
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Code or id not found!'})
#     except ValueError:
#         return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
#                         data={'error': 'value error'})