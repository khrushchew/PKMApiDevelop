from rest_framework import serializers

from Core.models.Device import Device

class AuthDeviceApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('company', 'code',)
