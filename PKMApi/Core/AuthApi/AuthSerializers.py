from rest_framework import serializers
from ..models.User import User

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'role', 'is_activated', 'profile_picture')