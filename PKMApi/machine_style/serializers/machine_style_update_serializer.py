from rest_framework import serializers

from Core.models.MachineStyle import MachineStyle


class MachineStyleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineStyle
        fields = ('name',)

    def validate_name(self, value):
        if MachineStyle.objects.filter(company=self.context.get('request').user.company, name=value).exists():
            raise serializers.ValidationError({'detail': 'Такой вид оборудования уже существует'})
        else:
            return value
        