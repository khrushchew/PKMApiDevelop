from rest_framework import serializers

from Core.models.Platform import Platform


class PlatformCreateApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('id', 'indent', 'name', 'address', 'company')