from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth import authenticate

from Core.models.User import User


class AuthUserApiSerializer(ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Неверные учетные данные')

        if not user.is_active:
            raise AuthenticationFailed('Пользователь не активирован')

        attrs['user'] = user
        return attrs
