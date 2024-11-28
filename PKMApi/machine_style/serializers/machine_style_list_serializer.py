from rest_framework import serializers

from Core.models.MachineStyle import MachineStyle
from Core.models.MachineName import MachineName


class MachineStyleListSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField(method_name='get_count')


    class Meta:
        model = MachineStyle
        fields = ('pk', 'name', 'count')

    def get_count(self, obj):
        return MachineName.objects.filter(company=self.context.get('request').user.company, type__group__style=obj).count()
    