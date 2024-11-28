from rest_framework import serializers

from Core.models.MachineGroup import MachineGroup


class MachineGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineGroup
        fields = ('name', 'style')

    def validate_name(self, value):
        if MachineGroup.objects.filter(style__company=self.context.get('request').user.company, name=value):
            raise serializers.ValidationError({'detail': 'Такая группа оборудования уже существует'})
        else:
            return value
