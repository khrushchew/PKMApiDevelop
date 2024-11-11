from rest_framework import serializers

from Core.models.MachineName import MachineName


class MachineNameApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineName
        fields = ("pk", "inv_number", "machine_code", "name", "surname", "img", "ratio", "tarife", "work_time", "company", "style", "group", "type", "machine_control_method", "platform", "department", "area", "brigade")
