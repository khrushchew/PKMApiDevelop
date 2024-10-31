from rest_framework import serializers

from Core.models.MachineName import MachineName


class MachineNameApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineName
        fields = '__all__'
