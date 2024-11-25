from rest_framework import serializers

from Core.models.Platform import Platform


class PlatformUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('indent', 'name', 'address')
