from rest_framework import serializers

from Core.models.MachineStyle import MachineStyle


class MachineStyleApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineStyle
        fields = ('pk', 'name', 'company')