from rest_framework import serializers

from Core.models.User import User


class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'name', 'surname', 'second_name', 'profile_picture', 'login', 'password', 'subdivision', 'position', 'role_1', 'role_2', 'is_activated')
