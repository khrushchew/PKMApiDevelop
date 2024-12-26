from rest_framework import serializers

from Core.models.Device import Device

class AuthDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('code',)
