from rest_framework import serializers

from Core.models.MachineName import MachineName


class MachineNameDetailApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineName
        fields = ("pk", "inv_number", "machine_code", "name", "surname", "area", "type")
