from rest_framework import serializers

from Core.models.MachineType import MachineType


class MachineTypeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineType
        fields = ('pk', 'name', 'group')
