from rest_framework import serializers

from Core.models.Platform import Platform


class PlatformApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ('pk', 'indent', 'name', 'address', 'company')