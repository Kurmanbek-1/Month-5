from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserLoginvalidateSerialzer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        """ Custom Validtion method """
        return password


class UserCreateValidateSerializer(serializers.Serializer):
    id_active = serializers.BooleanField(required=True)
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Пользователь уже существует!")
