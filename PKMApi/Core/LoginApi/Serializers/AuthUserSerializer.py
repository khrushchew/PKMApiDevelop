from rest_framework.serializers import ModelSerializer

from Core.models.User import User


class AuthUserApiSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'password')
