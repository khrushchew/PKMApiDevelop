from rest_framework import serializers

from Core.models.MachineGroup import MachineGroup


class MachineGroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineGroup
        fields = ('name', 'style')
        
    def validate_name(self, value):
        if MachineGroup.objects.filter(company=self.context.get('request').user.company, name=value).exists():
            raise serializers.ValidationError({'detail': 'Такая группа оборудования уже существует'})
        else:
            return value
