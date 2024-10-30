from rest_framework import serializers

from Core.models.MachineGroup import MachineGroup


class MachineGroupApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineGroup
        fields = ('pk', 'name', 'style')