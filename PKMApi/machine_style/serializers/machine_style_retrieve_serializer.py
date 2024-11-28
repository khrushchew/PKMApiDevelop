from rest_framework import serializers

from Core.models.MachineStyle import MachineStyle


class MachineStyleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineStyle
        fields = ('pk', 'name')
