from rest_framework import serializers

from Core.models.MachineGroup import MachineGroup


class MachineGroupRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineGroup
        fields = ('pk', 'name')
