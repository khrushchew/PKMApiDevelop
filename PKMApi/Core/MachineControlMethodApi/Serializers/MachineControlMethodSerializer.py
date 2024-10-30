from rest_framework import serializers

from Core.models.MachineControlMethod import MachineControlMethod


class MachineControlMethodApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineControlMethod
        fields = ('pk', 'company', 'name')
