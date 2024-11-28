from rest_framework import serializers

from Core.models.MachineGroup import MachineGroup
from Core.models.MachineName import MachineName


class MachineGroupListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(method_name='get_count')

    class Meta:
        model = MachineGroup
        fields = ('pk', 'name', 'count')

    def get_count(self, obj):
        return MachineName.object.filter(company=self.context.get('request').user.company, type__group=obj).count()
