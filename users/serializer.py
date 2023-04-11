from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import ConfirmUser


class UserLoginvalidateSerialzer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        """ Custom Validtion method """
        return password


class UserCreateValidateSerializer(serializers.Serializer):
    id_active = serializers.BooleanField(required=False, default=False)
    username = serializers.CharField()
    password = serializers.IntegerField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Пользователь уже существует!")

# -----------------------------------------------------------------------------------------------
class ConfirmUserValidateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_user_id(self, user_id):
        try:
            ConfirmUser.objects.get(id=user_id)
        except ConfirmUser.DoesNotExist:
            return user_id
        raise ValidationError("User_id does not exists!")


