from rest_framework import serializers

from Core.models.User import User


class LogoutUserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
